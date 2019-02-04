from typing import List
from pht.internal.describe.property.EnvironmentVariableProperty import \
    UrlEnvironmentVariableProperty, \
    TokenEnvironmentVariableProperty, \
    EnumEnvironmentVariableProperty

def url_by_name(name: str):
    return UrlEnvironmentVariableProperty(name)


def token_by_name(name: str):
    return TokenEnvironmentVariableProperty(name)


def enum_by_name(name: str, choices: List[str]):
    return EnumEnvironmentVariableProperty(name, choices)
