import torch
import torchvision.transforms as T
from PIL import Image, ImageDraw, ImageFont
import constants as C
from model import ShipClassifier
import yaml

def load_model(config, model_path):
    """
    Load the trained model from a checkpoint.
    """
    device = torch.device(config["train"]["device"])
    model = ShipClassifier(config).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model, device

def preprocess_image(image_path, transform):
    """
    Load and preprocess the full test image.
    """
    image = Image.open(image_path).convert("RGB")
    return image, transform

def crop_cells(image):
    """
    Extract 28 individual cells from the board image with extra padding.
    """
    cell_images = []
    cell_coords = []

    for row in range(len(C.row_names)):
        for col in range(len(C.col_names)):
            x1, x2 = C.col_borders[col] - C.offset, C.col_borders[col + 1] + C.offset
            y1, y2 = C.row_borders[row] - C.offset, C.row_borders[row + 1] + C.offset
            cell = image.crop((x1, y1, x2, y2))
            cell_images.append(cell)
            cell_coords.append((x1, y1, x2, y2))

    return cell_images, cell_coords

def predict_cells(model, device, cell_images, transform):
    """
    Run inference on individual cells and return predictions.
    """
    cell_tensors = torch.stack([transform(cell) for cell in cell_images]).to(device)

    with torch.no_grad():
        outputs = model(cell_tensors)
        predictions = torch.argmax(outputs, dim=1).cpu().numpy()

    return predictions

def interpret_results(predictions, cell_coords):
    """
    Interpret model predictions and determine the final decision for the board.
    """
    ship_detected = False
    detected_ship_info = None
    detected_ship_box = None

    for i, pred in enumerate(predictions):
        ship_type_idx = pred // 2
        heading_idx = pred % 2

        if ship_type_idx != C.ship_types["Empty"]:
            ship_detected = True
            cell_name = C.rect_names[i]
            ship_type = list(C.ship_types.keys())[ship_type_idx]
            heading = list(C.headings.keys())[heading_idx]
            detected_ship_info = f"Ship '{ship_type}' at {cell_name}, heading {heading}"
            detected_ship_box = cell_coords[i]
            break

    if ship_detected:
        return detected_ship_info, detected_ship_box
    return "No ships detected", None

def draw_results(image, detected_ship_info, detected_ship_box):
    """
    Draw the detected ship and verdict on the image.
    """
    image_with_text = Image.new("RGB", (image.width, image.height + 50), (255, 255, 255))
    image_with_text.paste(image, (0, 0))

    draw = ImageDraw.Draw(image_with_text)
    font_size = 20

    font = ImageFont.load_default()

    if detected_ship_box:
        draw.rectangle(detected_ship_box, outline="red", width=3)
        draw.text((detected_ship_box[0] + 5, detected_ship_box[1] + 5), "Ship", fill="red", font=font)

    text_position = (10, image.height + 10)
    draw.text(text_position, detected_ship_info, fill="black", font=font)

    return image_with_text

def run_inference(image_path, model_path, config_path):
    """
    Run inference pipeline on a single image and visualize results.
    """
    config = yaml.safe_load(open(config_path))
    model, device = load_model(config, model_path)

    transform = T.Compose([
        T.Resize((config["dataset"]["resize"], config["dataset"]["resize"])),
        T.ToTensor()
    ])

    image, _ = preprocess_image(image_path, transform)
    cell_images, cell_coords = crop_cells(image)
    predictions = predict_cells(model, device, cell_images, transform)

    detected_ship_info, detected_ship_box = interpret_results(predictions, cell_coords)

    image_with_results = draw_results(image, detected_ship_info, detected_ship_box)
    image_with_results.show()

    return detected_ship_info


if __name__ == "__main__":
    image_path = "../data/set-B_test/20171105_213603_Location-3C_Heading-East_Ship-Fishing-2.jpg"
    model_path = "../models/best_model.pth"
    config_path = "config.yaml"

    run_inference(image_path, model_path, config_path)