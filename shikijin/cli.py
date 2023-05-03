from argparse import ArgumentParser
from .worker import ShikijinWorker


def generate_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    worker_parser = subparsers.add_parser("worker")
    worker_parser.add_argument("--settings", type=str)
    return parser


def main() -> None:
    parser = generate_argument_parser()
    args = parser.parse_args()

    if args.command == "worker":
        worker = ShikijinWorker()
        worker.execute()
