"""
Contains helpers for type checking
"""
from typing import Any


def is_primitive(value: Any) -> bool:
    """
    Checks whether x is str, bool, int, float or None
    :param value: value to be tested
    :return: Whether value is primitive
    """
    return value is None or isinstance(value, (str, bool, int, float))


def is_list(value: Any) -> bool:
    """
    Checks whether the provided value is a list (in the sense of the list class, not the abc Sequence).
    :param value: Value to
    :return: True if value is a list
    """
    return isinstance(value, list)


def is_simple_dict(value: Any) -> bool:
    """
    Checks whether the provided value is a simple dict. A dictionary is called Simple if all keys
    are str and all values are either primitives, simple dicts, or lists of primitives or simple dicts.
    :param value: The value to be tested
    :return: True if value is a simple dict
    """
    def is_simple_list(item):
        return is_list(item) and all((is_primitive(x) or is_simple_dict(x) or is_simple_list(x) for x in item))

    if not isinstance(value, dict):
        return False
    for (key, val) in value.items():
        # Wrong type for key
        if not isinstance(key, str):
            return False
        # Wrong type for value
        if not is_primitive(val) and not is_simple_list(val) and not is_simple_dict(val):
            return False
    return True
