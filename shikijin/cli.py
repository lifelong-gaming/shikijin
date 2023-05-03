from argparse import ArgumentParser
from .settings import GlobalSettings
from .workers.factory import WorkerFactory


def generate_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--setting_file_path")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("worker")
    return parser


def main() -> None:
    parser = generate_argument_parser()
    args = parser.parse_args()

    if args.setting_file_path:
        global_settings = GlobalSettings(_env_file=args.setting_file_path)
    else:
        global_settings = GlobalSettings()
    if args.command == "worker":
        factory = WorkerFactory()
        worker = factory.create(global_settings)
        worker.execute()
