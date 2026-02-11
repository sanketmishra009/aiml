import argparse

parser = argparse.ArgumentParser(
    description="Train a machine learning model",
    epilog="""
Examples:
  python train.py --learning-rate 0.01 --epochs 100 \n
  python train.py --lr 0.001 --epochs 200 --model rf \n
  python train.py --help
    """,
)

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
    required=False,
    help="fix the # of epochs to train the model on!",
)

# parse arguments:

args = parser.parse_args()

print(f"Training configuration")
print(f"    Learning-rate: {args.learning_rate}")
print(f"    Epochs: {args.epoch}")
