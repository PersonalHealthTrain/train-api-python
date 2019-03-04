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
