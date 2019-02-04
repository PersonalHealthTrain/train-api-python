"""
PropertyState captures the State of the Property at runtime
"""
from typing import Optional
from pht.internal.protocols import Comparable, Copyable, DictRepresentable


class PropertyState(Copyable, Comparable, DictRepresentable):
    def __init__(self, is_available: bool, reason: Optional[str]):
        self._is_available = is_available
        self._reason = reason

    def dict(self):
        return {
            'isAvailable': self._is_available,
            'reason': self._reason
        }

    def copy(self):
        return PropertyState(self._is_available, self._reason)

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, PropertyState):
            return False
        return self._is_available == other._is_available and self._reason == other._reason

    def __hash__(self):
        return hash((self._is_available, self._reason))


PROPERTY_AVAILABLE = PropertyState(True, None)


class PropertyUnavailable(PropertyState):
    def __init__(self, reason: str):
        if not isinstance(reason, str):
            raise TypeError("'reason' of PropertyUnavailable must be a string.")
        super().__init__(is_available=False, reason=reason)
