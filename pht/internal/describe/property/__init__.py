from .EnvironmentVariableProperty import UrlEnvironmentVariableProperty
from .Property import Property


def url_by_name(name: str):
    return UrlEnvironmentVariableProperty(name)
