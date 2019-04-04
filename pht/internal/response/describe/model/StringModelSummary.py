"""
Contains the class: StringModelSummary
"""
from collections.abc import Hashable
from pht.internal.util import require

from .ModelSummary import ModelSummary


class StringModelSummary(Hashable, ModelSummary):
    """A Model Summary that is present as a str object"""
    def __init__(self, val: str):
        self._val = val
        require.type_is_str(self._val)

    def deepcopy(self):
        """Returns a Deep Copy of this StringModelSummary"""
        return StringModelSummary(self._val)

    def __hash__(self):
        return hash(self._val)

    @property
    def value(self):
        """Returns the value of this StringModelSummary"""
        return self._val
