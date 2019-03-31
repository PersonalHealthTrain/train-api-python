"""
Contains helpers for type checking.

These helpers are generally specializations of isinstance
"""
from typing import Any, Hashable, Mapping


def is_primitive(value: Any) -> bool:
    """
    Checks whether x is str, bool, int, float or None
    """
    return value is None or isinstance(value, (str, bool, int, float))


def is_list(value: Any) -> bool:
    """
    Checks whether the provided value is a list (in the sense of the list class, not the abc Sequence).
    """
    return isinstance(value, list)


def is_mapping(value: Any) -> bool:
    """
    Checks whether provided value is Mapping
    """
    return isinstance(value, Mapping)


def is_str(value: Any) -> bool:
    """
    Checks whether the provided value is a str.
    """
    return isinstance(value, str)


def is_hashable(value: Any) -> bool:
    """
    Checks whether provided value is Hashable
    """
    return isinstance(value, Hashable)
