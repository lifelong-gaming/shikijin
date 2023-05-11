from argparse import ArgumentParser

from .loggers.factory import LoggerFactory
from .settings import GlobalSettings
from .workers.factory import WorkerFactory


def generate_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--setting_file_path")
    subparsers = parser.add_subparsers(dest="command")
    worker_parser = subparsers.add_parser("worker")
    worker_parser.add_argument("--worker-name")
    return parser


def main() -> None:
    parser = generate_argument_parser()
    args = parser.parse_args()

    if args.setting_file_path:
        raise NotImplementedError()
    else:
        global_settings = GlobalSettings()

    logger = LoggerFactory().create(global_settings)

    if args.command == "worker":
        if args.worker_name is not None:
            global_settings.worker_settings["name"] = args.worker_name
        WorkerFactory(logger=logger).create(global_settings).main()
