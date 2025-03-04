import torch.nn as nn
import torchvision.models as models


class ShipClassifier(nn.Module):
    def __init__(self, config):
        num_classes = config["dataset"]["num_classes"]
        dropout_rate = config["model"]["dropout"]
        hidden_dim = config["model"]["hidden_dim"]

        super(ShipClassifier, self).__init__()
        self.backbone = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.DEFAULT)
        feature_size = self.backbone.classifier[0].in_features
        self.backbone.classifier = nn.Identity()
        self.classifier = nn.Sequential(
            nn.Linear(feature_size, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_dim, num_classes)
        )

    def forward(self, x):
        features = self.backbone(x)
        out = self.classifier(features)
        return out
