"""
Contains the BindMountEnvironmentVariableProperty class
"""
import enum
import os
from typing import Optional
from .EnvironmentVariableProperty import EnvironmentVariableProperty
from ..PropertyState import PropertyState


class MountType(enum.Enum):
    """The type of the mounted object"""
    FILE = 'file'
    DIRECTORY = 'directory'


class BindMountEnvironmentVariableProperty(EnvironmentVariableProperty):
    """A BindMountEnvironmentVariableProperty is an environment variable that points to a file or directory in the file
    system"""
    def __init__(self, name: str, description: Optional[str], mount_type: MountType):
        super().__init__(name, description)
        self.mount_type = mount_type

    def deepcopy(self):
        """Returns a Deep Copy this BindMountEnvironmentVariableProperty"""
        return BindMountEnvironmentVariableProperty(self.name, self.description, self.mount_type)

    def __repr__(self):
        return 'BindMount[name={},mountType={}]'.format(self.name, self.mount_type.value)

    def __hash__(self):
        return hash((self.name, self.mount_type))

    @property
    def data(self):
        """The data of the Bind Mount environment variable property"""
        _data = super().data
        _mount_type = 'mountType'
        if _mount_type in _data.keys():
            raise TypeError('Implementation Error: Key \'{}\' already defined in parent class.'.format(_mount_type))
        _data[_mount_type] = self.mount_type.value
        return _data

    def state(self) -> PropertyState:
        """A BindMountEnvironment variable is available if the file or directory exists in the file system"""
        _state = super().state()
        if not _state.is_satisfied:
            return _state
        value = self.get_value()
        if not os.path.exists(value):
            return PropertyState(
                is_satisfied=False,
                reason='The value \'{}\' is not an existing path in the file system'.format(value))
        if not os.path.isfile(value) and self.mount_type == MountType.FILE:
            return PropertyState(
                is_satisfied=False,
                reason='The value \'{}\' is not a file, but it should be'.format(value))
        if not os.path.isdir(value) and self.mount_type == MountType.DIRECTORY:
            return PropertyState(
                is_satisfied=False,
                reason='The value \'{}\' is not a directory, but it should be'.format(value))
        return PropertyState(is_satisfied=True)
