import argparse
import sys
from .chat import chat
from .model_manager import switch_model


KNOWN_COMMANDS = ["chat", "model"]


def main():

    parser = argparse.ArgumentParser(
        description="CLI llm tool.",
        epilog="""
    myllm chat "Explain transformers"
    myllm model switch mistral
    myllm chat --stream "Hello"

                                    """,
    )

    subparsers = parser.add_subparsers(dest="command", help="" "Available commands")

    # chat parser:

    chatparser = subparsers.add_parser(
        "chat", help="" "Tool to chat with different llm models."
    )
    chatparser.add_argument("chat", default=True, type=str, nargs="+")

    # model command:

    modelparser = subparsers.add_parser("model", help="help configure the models.")
    modelparser.add_argument(
        "--model-name", choices=["qwen", "llama", "mistral"], default="llama", type=str
    )

    if len(sys.argv) > 1 and sys.argv[1] not in KNOWN_COMMANDS:
        sys.argv.insert(1, "chat")

    args = parser.parse_args()
    print(args)

    if args.command is None or args.command == "chat":
        text = " ".join(args.chat)
        chat(text)
    else:
        switch_model(args.model_name)


if __name__ == "__main__":
    main()
