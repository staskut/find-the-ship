import os
import yaml

from dotenv import load_dotenv
import mlflow
from torchinfo import summary

from dataset import prepare_datasets, compute_class_weights
from model import ShipClassifier
from train import train

load_dotenv(".env")
config = yaml.safe_load(open('config.yaml'))

if __name__ == '__main__':
    mlflow.set_tracking_uri(os.environ.get("MLFLOW_TRACKING_URI"))
    mlflow.set_experiment(config["mlflow"]["experiment_name"])
    mlflow.start_run(run_name=config["mlflow"]["run_name"])
    mlflow.log_params(config)

    train_dataloader, val_dataloader, test_dataloader = prepare_datasets(config)
    model = ShipClassifier(config)
    summary_str = str(summary(model))
    with open("model_summary.txt", "w") as f:
        f.write(summary_str)
    mlflow.log_artifact("model_summary.txt")

    class_weights = compute_class_weights(train_dataloader.dataset)
    mlflow.log_params({"class_weights": class_weights})

    train(model, train_dataloader, val_dataloader, class_weights, config)

    mlflow.end_run()