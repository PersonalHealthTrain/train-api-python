import abc
from pht.internal.protocol.DictRepresentable import DictRepresentable
from pht.internal.util.require import not_in
from pht.internal.util import require


class Typed(DictRepresentable):

    @property
    @abc.abstractmethod
    def type(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def type_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def data(self) -> dict:
        pass

    def as_dict(self) -> dict:
        # Meta Keys for the Type
        _type = 'type'
        _typeName = 'typeName'
        _typeSystem = 'typeSystem'

        data = self.data
        require.for_each_value(
            inside=[_type, _typeName, _typeSystem],
            that=not_in(data.keys()),
            error_if_not='Key \'{}\' not allowed in data dictionary of class')
        data[_type] = self.type
        data[_typeName] = self.type_name
        data[_typeSystem] = 'pythonclass'
        return data
