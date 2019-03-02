from typing import Any, Iterable


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


def for_each_value(inside: Iterable[Any], that, error_if_not: str):
    for i in inside:
        for_value(i, that, error_if_not.format(i))


def for_value(val, that, error_if_not):
    if not that(val):
        raise ValueError(error_if_not)


def is_not_none(val) -> bool:
    return val is not None


def is_positive(val: int) -> bool:
    return val > 0


def is_in_closed_range(start, end):
    return lambda val: val in range(start, end + 1)


def not_in(collection):
    return lambda val: val not in collection


def that(test: bool, error_if_not):
    if not test:
        raise ValueError(error_if_not)
