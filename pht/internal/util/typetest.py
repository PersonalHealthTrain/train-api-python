"""
Contains helpers for type checking
"""
from typing import Any, Mapping
from collections.abc import Hashable


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
    """
    return isinstance(value, list)


def is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def is_str(value: Any) -> bool:
    """
    Checks whether the provided value is a str.
    """
    return isinstance(value, str)


def is_hashable(value: Any) -> bool:
    return isinstance(value, Hashable)
