"""
Utility functions

@author: Lukas Zimmermann
"""


def value_error_if(test: bool, msg: str):
    if test:
        raise ValueError(msg)
