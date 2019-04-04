"""
Contains the TypeSystem class
"""
from collections.abc import Hashable
from pht.internal.protocol.DeepCopyable import DeepCopyable
from pht.internal.protocol.SimpleMappingRepresentable import SimpleMappingRepresentable


class TypeSystem(DeepCopyable, Hashable, SimpleMappingRepresentable):
    """The TypeSystem"""
    def __init__(self, name: str, version: str):
        self._name = name
        self._version = version

    @property
    def name(self):
        """Name of the TypeSystem"""
        return self._name

    @property
    def version(self):
        """Version of the TypeSystem"""
        return self._version

    def _as_dict(self) -> dict:
        return {
            'name': self._name,
            'version': self._version
        }

    def deepcopy(self):
        """Makes a Copy of the type system"""
        return TypeSystem(self._name, self._version)

    def __hash__(self) -> int:
        return hash((self._name, self._version))
