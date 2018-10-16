"""
Module for accessing the train environment

"""
import os
from .util import ensure_no_trailing_slashes


def env_exists(key: str) -> bool:
    """
    Checks whether key exists in environment
    :param key: The str key to check whethet is exists in environment
    :return: True if key exists in environment, else False
    """
    return key in os.environ


def from_env(key: str) -> str:
    return os.environ[key]


def from_env_without_trailing_slashes(key: str) -> str:
    return ensure_no_trailing_slashes(from_env(key))
