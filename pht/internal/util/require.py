from typing import Any


def _type_error_if(test: bool, msg: str):
    if test:
        raise TypeError(msg)


def type_is_int(obj: Any):
    _type_error_if(
        not isinstance(obj, int) or isinstance(obj, bool),
        "Object '{}' is required to be of type 'int' (and also not of type bool)".format(str(obj)))


def type_is_str(obj: Any):
    _type_error_if(
        not isinstance(obj, str),
        'Object \'{}\' is required to be of type \'str\''.format(str(obj)))


def for_value(val, func, msg):
    if not func(val):
        raise ValueError(msg)


def is_not_none(val):
    return val is not None
