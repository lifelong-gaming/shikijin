from logging import Formatter

class JsonFormatter(Formatter):
    def __init__(self, fmt: str, json_ensure_ascii: bool): ...
