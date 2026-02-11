import argparse

parser = argparse.ArgumentParser(description="Train a machine learning model")

# add arguments:

parser.add_argument(
    "--learning-rate",
    "-lr",
    type=float,
    required=True,
    help="fix the learning rate on which the model would be trained!",
)

parser.add_argument(
    "--epoch",
    "-e",
    type=int,
    required=True,
    help="fix the # of epochs to train the model on!",
)

# parse arguments:

args = parser.parse_args()

print(f"Training configuration")
print(f"    Learning-rate: {args.learning_rate}")
print(f"    Epochs: {args.epochs}")
