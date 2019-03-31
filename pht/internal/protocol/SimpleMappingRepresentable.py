"""
Contains the protocol class: SimpleMappingRepresentable
"""
from abc import ABC, abstractmethod
from typing import Any
from types import MappingProxyType
from pht.internal.util.typetest import is_list, is_mapping, is_primitive, is_str


class SimpleMappingRepresentable(ABC):
    """
    Classes implementing this protocol have a canonical representation of a simple mapping.
    The pht library defines a Python Mapping to be 'simple' if all keys are str objects and the each value is either
    None, int, float, bool, str, a simple mapping or a list thereof.

    Equality of two objects, which are SimpleMappingRepresentable, should be determined by the representation as simple
    mapping. Hence, two SimpleMappingRepresentable objects are equal if and only if their respective representations
    as simple mappings are equal. Equality on simple mappings is well-defined, since any value cannot be an object for
    which equality is undefined.

    Furthermore, for a SimpleMappingRepresentable object x, the resulting JSON object returned by json.dump(x) is fully
    determined.
    """
    def as_simple_mapping(self) -> MappingProxyType:
        """
        Returns SimpleMapping view of this object
        """
        dict_repr = self._as_dict()
        if not SimpleMappingRepresentable.is_simple_mapping(dict_repr):
            raise TypeError("Mapping is not simple!")
        return MappingProxyType(dict_repr)

    @abstractmethod
    def _as_dict(self) -> dict:
        """
        Protected. Returns representation of this object as simple dictionary.
        :return: This object represented as a simple dictionary.
        """
        pass

    def __eq__(self, other):
        return other is self or \
               isinstance(other, SimpleMappingRepresentable) and self.as_simple_mapping() == other.as_simple_mapping()

    @staticmethod
    def is_simple_mapping(value: Any) -> bool:
        """
        Checks whether the provided value is a simple dict. A dictionary is called Simple if all keys
        are str and all values are either primitives, simple dicts, or lists of primitives or simple dicts.
        :param value: The value to be tested
        :return: True if value is a simple dict
        """
        def is_simple_list(item: Any) -> bool:
            """Checks whether input object is a simple list"""
            return is_list(item) and all(
                is_primitive(x) or
                SimpleMappingRepresentable.is_simple_mapping(x) or
                is_simple_list(x) for x in item)

        def inner(inner_value: Any) -> bool:
            """
            Checks whether inner_value is a SimpleMapping
            """
            if not is_mapping(inner_value):
                return False
            for (key, val) in inner_value.items():
                # Wrong type for key or value
                if not (is_str(key) and (is_primitive(val) or is_simple_list(val) or inner(val))):
                    return False
            # All dictionary items have correct type
            return True
        return inner(value)
