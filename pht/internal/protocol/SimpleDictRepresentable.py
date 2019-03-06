import abc
from pht.internal.util.typetest import is_simple_dict


class SimpleDictRepresentable(abc.ABC):
    """
    Classes implementing this protocol have a canonical represenation as a dictionary
    """
    def as_simple_dict(self) -> dict:
        d = self._as_dict()
        if not is_simple_dict(d):
            raise TypeError("Dictionary is not simple!")
        return d

    @abc.abstractmethod
    def _as_dict(self) -> dict:
        pass

    def __eq__(self, other):
        return other is self or \
               isinstance(other, SimpleDictRepresentable) and self.as_simple_dict() == other.as_simple_dict()
