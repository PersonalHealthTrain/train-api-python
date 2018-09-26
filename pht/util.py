"""
Utility functions

@author: Lukas Zimmermann
"""
from .types import AnyDict


def value_error_if(test: bool, msg: str):
    """
    Raises value error if provided test is true
    :param test: Whether value error is to be raised
    :param msg: The message that is associated with the value error
    """
    if test:
        raise ValueError(msg)


def without_none_values(d: AnyDict) -> AnyDict:
    """
    Removes all mappings from the dictionary where the value is `None`.
    :param d: The dictionary to clear from `None` values
    :return: The input dictionary with all `None` values removed
    """
    return {key: value for key, value in d.items() if value is not None}
