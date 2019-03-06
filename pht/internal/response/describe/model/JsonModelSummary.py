from typing import Union
from pht.internal.protocol.Copyable import Copyable
from .ModelSummary import ModelSummary


class JsonModelSummary(ModelSummary):
    def __init__(self, val: Union[Copyable, dict, list]):
        self._val = val.copy()

    def copy(self):
        return JsonModelSummary(self._val)

    @property
    def value(self):
        return self._val
