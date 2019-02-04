import abc


class Copyable(abc.ABC):
    """
    Marks a class to be copyable and requires implementation of Copy.
    Generally, implementors should not distinguish between flat copy and
    deep copy.
    """
    @abc.abstractmethod
    def copy(self):
        pass

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()


class Comparable(abc.ABC):

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass


class DictRepresentable(abc.ABC):

    @abc.abstractmethod
    def dict(self):
        pass


class Typed(DictRepresentable):

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
