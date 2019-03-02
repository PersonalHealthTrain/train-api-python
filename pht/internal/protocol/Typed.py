import abc
from pht.internal.protocol.DictRepresentable import DictRepresentable


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

    def as_dict(self):
        # Meta Keys for the Type
        _type = 'type'
        _typeName = 'typeName'
        data = self.data
        for key in [_type, _typeName]:
            if key in data:
                raise TypeError('Key \'{}\' not allowed in data dictionary of class'.format(key))
        data[_type] = self.type
        data[_typeName] = self.type_name
        return data
