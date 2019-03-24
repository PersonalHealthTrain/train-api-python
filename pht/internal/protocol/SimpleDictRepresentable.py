from abc import ABC, abstractmethod
from typing import Any
from pht.internal.util.typetest import is_list, is_dict, is_primitive, is_str


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
        if not SimpleDictRepresentable.is_simple_dict(dict_repr):
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

    @staticmethod
    def is_simple_dict(value: Any) -> bool:
        """
        Checks whether the provided value is a simple dict. A dictionary is called Simple if all keys
        are str and all values are either primitives, simple dicts, or lists of primitives or simple dicts.
        :param value: The value to be tested
        :return: True if value is a simple dict
        """
        def is_simple_list(item):
            return is_list(item) and \
                   all((is_primitive(x) or
                        SimpleDictRepresentable.is_simple_dict(x) or
                        is_simple_list(x) for x in item))

        if not is_dict(value):
            return False
        for (key, val) in value.items():
            # Wrong type for key
            if not is_str(key):
                return False
            # Wrong type for value
            if not is_primitive(val) and not is_simple_list(val) and not SimpleDictRepresentable.is_simple_dict(val):
                return False
        # All dictionary items have correct type
        return True
