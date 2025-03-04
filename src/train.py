import matplotlib.pyplot as plt
import mlflow
from sklearn.metrics import f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import torch
from tqdm import tqdm

def train(model, train_loader, val_loader, class_weights, config):
    device = torch.device(config["train"]["device"])
    criterion = torch.nn.CrossEntropyLoss(class_weights.to(device))
    optimizer = torch.optim.Adam(model.parameters(), lr=config["train"]["lr"])
    epochs = config["train"]["epochs"]

    model.to(device)
    best_val_f1 = 0.0

    for epoch in tqdm(range(epochs), desc="Training", unit="epoch"):
        last_epoch = epoch == epochs - 1
        train_loss, train_f1 = train_epoch(model, train_loader, optimizer, criterion, device)
        val_loss, val_f1 = validate_epoch(model, val_loader, criterion, device, last_epoch)

        mlflow.log_metrics({
            "train_loss": train_loss,
            "train_f1": train_f1,
            "val_loss": val_loss,
            "val_f1": val_f1,
        }, step=epoch)

        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            torch.save(model.state_dict(), "../models/best_model.pth")

    mlflow.log_artifact("../models/best_model.pth")

def train_epoch(model, train_loader, optimizer, criterion, device):
    model.train()
    train_loss = 0
    all_train_preds, all_train_labels = [], []

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)

        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        preds = outputs.argmax(dim=1)

        all_train_preds.extend(preds.cpu().numpy())
        all_train_labels.extend(labels.cpu().numpy())

    train_f1 = f1_score(all_train_labels, all_train_preds, average="macro")
    avg_train_loss = train_loss / len(train_loader)

    return avg_train_loss, train_f1

def validate_epoch(model, val_loader, criterion, device, last_epoch):
    model.eval()
    val_loss = 0
    all_val_preds, all_val_labels = [], []

    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            val_loss += loss.item()
            preds = outputs.argmax(dim=1)

            all_val_preds.extend(preds.cpu().numpy())
            all_val_labels.extend(labels.cpu().numpy())

    val_f1 = f1_score(all_val_labels, all_val_preds, average="macro")
    avg_val_loss = val_loss / len(val_loader)

    if last_epoch:
        clf_report = classification_report(all_val_labels, all_val_preds, digits=4)
        with open("classification_report.txt", "w") as f:
            f.write(clf_report)
        mlflow.log_artifact("classification_report.txt")

        conf_matrix = confusion_matrix(all_val_labels, all_val_preds)
        disp = ConfusionMatrixDisplay(conf_matrix)
        disp.plot()
        plt.savefig("confusion_matrix.png")

        mlflow.log_artifact("confusion_matrix.png")

    return avg_val_loss, val_f1
