from collections.abc import Hashable
from pht.internal.protocol.DeepCopyable import DeepCopyable
from pht.internal.protocol.SimpleMappingRepresentable import SimpleMappingRepresentable


class TypeSystem(DeepCopyable, Hashable, SimpleMappingRepresentable):
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    def _as_dict(self) -> dict:
        return {
            'name': self.name,
            'version': self.version
        }

    def deepcopy(self):
        return TypeSystem(self.name, self.version)

    def __hash__(self) -> int:
        return hash((self.name, self.version))
