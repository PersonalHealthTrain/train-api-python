import abc


class Typed(abc.ABC):

    @property
    @abc.abstractmethod
    def type(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def display(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def data(self) -> dict:
        pass

    def dict(self):
        _type = 'type'
        _display = 'display'
        data = self.data
        for key in [_type, _display]:
            if key in data:
                raise TypeError('Key \'{}\' not allowed in data dictionary of class'.format(key))
        data[_type] = self.type
        data[_display] = self.display
        return data
