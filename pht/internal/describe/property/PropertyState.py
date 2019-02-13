"""
PropertyState captures the State of the Property at runtime
"""
from typing import Optional
from pht.internal.protocol import Comparable, Copyable, DictRepresentable


class PropertyState(Copyable, Comparable, DictRepresentable):
    def __init__(self, is_available: bool, reason: Optional[str]):
        self._is_available = is_available
        self._reason = reason

        if not isinstance(self._is_available, bool):
            raise TypeError('is_available must be a Boolean value')

        if not isinstance(self._reason, str) and self._reason is not None:
            raise TypeError('reason must be a str value or None')

    def as_dict(self):
        return {
            'isAvailable': self._is_available,
            'reason': self._reason
        }

    def copy(self):
        return PropertyState(self._is_available, self._reason)

    def __eq__(self, other):
        return other is self or \
               (isinstance(other, PropertyState) and
                self._is_available == other._is_available and self._reason == other._reason)

    def __hash__(self):
        return hash((self._is_available, self._reason))


PROPERTY_AVAILABLE = PropertyState(
    is_available=True,
    reason=None)


class PropertyUnavailable(PropertyState):
    def __init__(self, reason: str):
        if not isinstance(reason, str):
            raise TypeError("'reason' of PropertyUnavailable must be a string.")
        super().__init__(is_available=False, reason=reason)
