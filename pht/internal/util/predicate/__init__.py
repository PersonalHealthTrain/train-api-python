"""
Contains Predicates
"""


def is_not_none(x) -> bool:
    """
    Checks whether 'x' is not None
    """
    return x is not None


def is_positive(x: int) -> bool:
    """
    Checks whether int 'x' is positive (i.e. > 0)
    """
    return x > 0
