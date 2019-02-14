from typing import List
from .EnvironmentVariableProperty import EnvironmentVariableProperty
from .EnumEnvironmentVariableProperty import EnumEnvironmentVariableProperty
from .UrlEnvironmentVariableProperty import UrlEnvironmentVariableProperty
from .TokenEnvironmentVariableProperty import TokenEnvironmentVariableProperty


def url_by_name(name: str):
    return UrlEnvironmentVariableProperty(name)


def token_by_name(name: str):
    return TokenEnvironmentVariableProperty(name)


def enum_by_name(name: str, choices: List[str]):
    return EnumEnvironmentVariableProperty(name, choices)
