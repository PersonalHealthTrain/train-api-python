"""
Contains the class: JsonModelSummary
"""
from typing import Union
from copy import deepcopy
from pht.internal.protocol.DeepCopyable import DeepCopyable
from .ModelSummary import ModelSummary


class JsonModelSummary(ModelSummary):
    """The Model Summary which is represented as a JSON object"""
    def __init__(self, val: Union[DeepCopyable, dict, list]):
        self._val = deepcopy(val)

    def deepcopy(self):
        """Returns a Deep Copy of this JsonModelSummary"""
        return JsonModelSummary(self._val)

    @property
    def value(self):
        """The value of this JsonModelSummary"""
        return self._val
