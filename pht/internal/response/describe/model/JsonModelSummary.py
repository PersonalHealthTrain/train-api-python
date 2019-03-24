from typing import Union
from copy import deepcopy
from pht.internal.protocol.DeepCopyable import DeepCopyable
from .ModelSummary import ModelSummary


class JsonModelSummary(ModelSummary):
    def __init__(self, val: Union[DeepCopyable, dict, list]):
        self._val = deepcopy(val)

    def deepcopy(self):
        return JsonModelSummary(self._val)

    @property
    def value(self):
        return self._val
