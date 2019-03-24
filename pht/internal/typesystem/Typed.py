from abc import abstractmethod
from pht.internal.util import require
from pht.internal.util.require import not_in
from pht.internal.protocol.SimpleDictRepresentable import SimpleDictRepresentable
from pht.internal.protocol.DeepCopyable import DeepCopyable
from pht.internal.typesystem.TypeSystem import TypeSystem


class Typed(DeepCopyable, SimpleDictRepresentable):
    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def type_name(self) -> str:
        pass

    @property
    @abstractmethod
    def type_system(self) -> TypeSystem:
        pass

    @property
    @abstractmethod
    def data(self) -> dict:
        pass

    def _as_dict(self) -> dict:
        # Meta Keys for the Type
        _type = '@type'
        _typeName = '@typeName'
        _typeSystem = '@typeSystem'

        data = self.data
        require.for_each_value(
            inside=[_type, _typeName, _typeSystem],
            that=not_in(data.keys()),
            error_if_not='Key \'{}\' not allowed in data dictionary of class')
        data[_type] = self.type
        data[_typeName] = self.type_name
        data[_typeSystem] = self.type_system.as_simple_dict()
        return data
