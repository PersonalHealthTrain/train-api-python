"""
Utility functions

@author: Lukas Zimmermann
"""
from .types import AnyDict

SLASH = '/'


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


def ensure_no_trailing_slashes(s: str) -> str:
    """
    Removes all trailing '/' characters from s
    :param s: The str instance to be trimmed
    :return: s without the trailing slashes
    """
    return s.rstrip(SLASH)


def ensure_trailing_slash(s: str) -> str:
    """
    Ensures that the given str instance ends with a '/' character.
    Does nothing if 's' already ends on '/'
    :param s: The str instance to be ensured to end with a trailing '/' char
    :return: If s already ends with '/', then s is returned unaltered. Otherwise, return s + '/'
    """
    return s if s.endswith(SLASH) else s + SLASH
