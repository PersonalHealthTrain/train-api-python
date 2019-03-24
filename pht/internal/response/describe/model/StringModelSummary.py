from collections.abc import Hashable
from pht.internal.util import require

from .ModelSummary import ModelSummary


class StringModelSummary(Hashable, ModelSummary):
    def __init__(self, val: str):
        self._val = val
        require.type_is_str(self._val)

    def deepcopy(self):
        return StringModelSummary(self._val)

    def __hash__(self):
        return hash(self._val)

    @property
    def value(self):
        return self._val
