"""
Contains functions that return predicates upon invocation. Object to be tested if referred to as 'x'
"""
from typing import Any, Callable, Container
_predicate = Callable[[Any], bool]


def is_in_closed_range(start: int, stop: int) -> _predicate:
    """
    Makes predicate to check whether x is in closed range between start and end
    """
    return lambda x: x in range(start, stop + 1)


def not_in(container: Container) -> _predicate:
    """
    Makes predicate to check whether x is in container
    """
    return lambda x: x not in container


def does_not_contain(element: Any) -> _predicate:
    """
    Makes predicate to check whether x does not contain value
    """
    return lambda container: element not in container
