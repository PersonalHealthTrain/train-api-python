from typing import List, Optional
from .EnvironmentVariableProperty import EnvironmentVariableProperty
from .EnumEnvironmentVariableProperty import EnumEnvironmentVariableProperty
from .UrlEnvironmentVariableProperty import UrlEnvironmentVariableProperty
from .TokenEnvironmentVariableProperty import TokenEnvironmentVariableProperty
from .BindMountEnvironmentVariableProperty import BindMountEnvironmentVariableProperty, MountType


def url_by_name(name: str, description: Optional[str] = None):
    return UrlEnvironmentVariableProperty(name, description)


def token_by_name(name: str, description: Optional[str] = None):
    return TokenEnvironmentVariableProperty(name, description)


def enum_by_name(name: str, choices: List[str], description: Optional[str] = None):
    return EnumEnvironmentVariableProperty(name, description, choices)


def bind_mount_by_name(name: str, mount_type: MountType, description: Optional[str] = None):
    return BindMountEnvironmentVariableProperty(name, description, mount_type)
