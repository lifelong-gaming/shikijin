from ..base import EntryPointMixin
from ..components import BaseShikijinComponent


class BaseWorker(BaseShikijinComponent, EntryPointMixin):
    def __init__(self):
        ...
