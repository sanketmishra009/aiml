import argparse

parser = argparse.ArgumentParser(
    description="Tool for model training , testing , inference"
)

subparsers = parser.add_subparsers(dest="command", help="Available commands")


# train parser
trainparser = subparsers.add_parser("train", help="Tool to train a model")
trainparser.add_argument("--lr", type=float, required=True)
trainparser.add_argument("--epoch", type=int, required=True)
trainparser.add_argument("--model", choices=["rf", "lr", "nn"], default="nn")


# test parser
testparser = subparsers.add_parser("test", help="Test the model")
testparser.add_argument("--model-path", required=True, type=str)
testparser.add_argument("--output", default="prediction.csv")


args = parser.parse_args()
print(args)
