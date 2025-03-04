from collections import Counter
from pathlib import Path

from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader, random_split
import torchvision.transforms as T

import constants as C

class BoardDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.image_paths = list(Path(root_dir).glob("**/*.jpg"))
        self.transform = transform
        self.row_ticks = C.row_borders
        self.col_ticks = C.col_borders
        self.rect_names = C.rect_names

    def parse_filename(self, filename):
        """
        Extract target labels from filename. Two expected cases are:
         - 20171105_185402_Empty.jpg
         - 20171105_185419_Location-1B_Heading-East_Ship-Fishing-1.jpg

        Returns:
            location (str): The location of the ship.
            heading (str): The heading of the ship.
            ship_type (str): The type of the ship.
        """
        base_name = filename.stem.split("_")

        if "Empty" in base_name:
            return "Empty", None, None

        location = base_name[2].split("-")[1]
        heading = base_name[3].split("-")[1]
        ship_type = base_name[4].split("-", maxsplit=1)[1]

        return location, heading, ship_type

    def __len__(self):
        return len(self.image_paths) * C.cells_per_image

    def __getitem__(self, index):
        img_idx = index // C.cells_per_image
        cell_idx = index % C.cells_per_image

        img_path = self.image_paths[img_idx]
        image = Image.open(img_path).convert("RGB")

        row, col = divmod(cell_idx, len(C.col_names))
        x1, x2 = self.col_ticks[col] - C.offset, self.col_ticks[col + 1] + C.offset
        y1, y2 = self.row_ticks[row] - C.offset, self.row_ticks[row + 1] + C.offset

        cell_img = image.crop((x1, y1, x2, y2))

        if self.transform:
            cell_img = self.transform(cell_img)

        location, heading, ship_type = self.parse_filename(img_path)
        cell_name = self.rect_names[cell_idx]

        has_ship = location == cell_name
        if has_ship:
            heading_label = C.headings[heading]
            ship_type_label = C.ship_types[ship_type]
            label = ship_type_label * 2 + heading_label
        else:
            label = C.ship_types["Empty"] * 2

        return cell_img, label

def get_transforms(config):
    transform = T.Compose([
        T.Resize((config["dataset"]["resize"], config["dataset"]["resize"])),
        T.ToTensor()
    ])
    return transform

def prepare_datasets(config):
    """
    Splits the training dataset into training and validation sets,
    and creates DataLoaders for training, validation, and testing.

    Returns:
        train_dataloader (DataLoader): DataLoader for the training set.
        val_dataloader (DataLoader): DataLoader for the validation set.
        test_dataloader (DataLoader): DataLoader for the testing set.
    """
    data_params = config["dataset"]
    train_root, test_root = data_params["train_path"], data_params["test_path"]
    train_split = data_params["train_ratio"]
    batch_size = data_params["batch_size"]
    transform = get_transforms(config)

    train_dataset = BoardDataset(train_root, transform=transform)
    test_dataset = BoardDataset(test_root, transform=transform)

    train_size = int(len(train_dataset) * train_split)
    val_size = len(train_dataset) - train_size
    train_subset, val_subset = random_split(train_dataset, [train_size, val_size])

    train_dataloader = DataLoader(train_subset, batch_size=batch_size, shuffle=True, num_workers=6)
    val_dataloader = DataLoader(val_subset, batch_size=batch_size, shuffle=False, num_workers=6)
    test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=6)

    return train_dataloader, val_dataloader, test_dataloader


def compute_class_weights(train_dataset):
    """
    Compute class weights based on the training dataset frequencies.

    Returns:
        class_weights_tensor (torch.Tensor): The computed class weights.
    """
    class_counts = Counter()

    for _, label in train_dataset:
        class_counts[label] += 1

    total_samples = sum(class_counts.values())
    num_classes = len(class_counts)

    class_weights = {cls: total_samples / (num_classes * count) for cls, count in class_counts.items()}
    class_weights_tensor = torch.tensor([class_weights[i] for i in range(num_classes)], dtype=torch.float32)

    return class_weights_tensor