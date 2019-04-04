"""
Functions that raise ValueError or TypeError on test failure
"""
from typing import Any, Iterable
from pht.internal.util.typetest import is_str


def _error(when: bool, message: str, error):
    if when:
        raise error(message)


def _type_error(*, when: bool, message: str):
    _error(when, message, TypeError)


def _value_error(*, when: bool, message: str):
    _error(when, message, ValueError)


def type_is_int(obj: Any):
    """
    Checks whether object is int, and not bool
    """
    _type_error(
        when=not isinstance(obj, int) or isinstance(obj, bool),
        message="Object '{}' is required to be of type 'int' (and also not of type bool)".format(str(obj)))


def type_is_not_none(obj: Any):
    """Requires that obj is not null"""
    _type_error(
        when=obj is None,
        message='Object is none!')


def type_is_str(obj: Any):
    """
    Checks whether obj is str
    """
    _type_error(
        when=not is_str(obj),
        message='Object \'{}\' is required to be of type \'str\''.format(str(obj)))


def type_is_str_or_none(obj: Any):
    """Requires that the object is a str or None"""
    _type_error(
        when=obj is not None and not is_str(obj),
        message='Object \'{}\' is required to be None or of type \'str\''.format(str(obj)))


def value_is_positive(value: Any):
    _value_error(
        when=value <= 0,
        message='Object \'{}\' is not positive')


def for_each_value(inside: Iterable[Any], that, error_if_not: str):
    for i in inside:
        for_value(i, that, error_if_not.format(i))


def for_value(val, that, error_if_not):
    if not that(val):
        raise ValueError(error_if_not)


def that(test: bool, error_if_not):
    if not test:
        raise ValueError(error_if_not)
