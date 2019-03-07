from abc import ABC, abstractmethod
from pht.internal.util.typetest import is_simple_dict


class SimpleDictRepresentable(ABC):
    """
    Classes implementing this protocol have a canonical representation of a simple dictionary.
    The pht library defines a Python dictionary to be 'simple' if all keys are str objects and the each value is either
    None, int, float, bool, str, a simple dict or a list thereof.

    Equality of two objects, which are SimpleDictRepresentable, should be determined by the representation as simple
    dictionary. Hence, two SimpleDictRepresentable objects are equal if and only if their representation as simple
    dictionary is equal. Equality on simple dictionaries is well-defined, since values cannot be objects for
    which equality is undefined.

    Furthermore, for a SimpleDictRepresentable object x, the resulting JSON object returned by json.dump(x) is
    determined.
    """
    def as_simple_dict(self) -> dict:
        dict_repr = self._as_dict()
        if not is_simple_dict(dict_repr):
            raise TypeError("Dictionary is not simple!")
        return dict_repr

    @abstractmethod
    def _as_dict(self) -> dict:
        """
        Protected. Returns representation of this object as simple dictionary.
        :return: This object represented as a simple dictionary.
        """
        pass

    def __eq__(self, other):
        return other is self or \
               isinstance(other, SimpleDictRepresentable) and self.as_simple_dict() == other.as_simple_dict()
