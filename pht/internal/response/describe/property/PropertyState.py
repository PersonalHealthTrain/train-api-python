"""
PropertyState captures the State of the Property at runtime
"""
from pht.internal.protocol.DeepCopyable import DeepCopyable
from pht.internal.protocol.SimpleMappingRepresentable import SimpleMappingRepresentable
from pht.internal.util import require


class PropertyState(SimpleMappingRepresentable, DeepCopyable):
    """Represents the state of a property at runtime"""
    def __init__(self, *, is_satisfied: bool, reason: str = ''):
        self._is_satisfied = is_satisfied
        self._reason = reason
        require.type_is_bool(is_satisfied)
        require.type_is_str(reason)

    @property
    def is_satisfied(self) -> bool:
        """Whether the property is satisfied"""
        return self._is_satisfied

    @property
    def reason(self) -> str:
        """The reason for the property being satisfied or not"""
        return self._reason

    def _as_dict(self):
        return {
            'isAvailable': self._is_satisfied,
            'reason': self._reason
        }

    def deepcopy(self):
        """Returns Deep Copy of this Property State"""
        return PropertyState(
            is_satisfied=self._is_satisfied,
            reason=self._reason)

    def __hash__(self):
        return hash((self._is_satisfied, self._reason))
