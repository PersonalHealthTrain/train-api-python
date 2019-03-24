import enum
import os
from typing import Optional
from .EnvironmentVariableProperty import EnvironmentVariableProperty
from ..PropertyState import PropertyState, PropertyUnavailable, PROPERTY_AVAILABLE


class MountType(enum.Enum):
    FILE = 'file'
    DIRECTORY = 'directory'


class BindMountEnvironmentVariableProperty(EnvironmentVariableProperty):

    def __init__(self, name: str, description: Optional[str], mount_type: MountType):
        super().__init__(name, description)
        self.mount_type = mount_type

    def deepcopy(self):
        return BindMountEnvironmentVariableProperty(self.name, self.description, self.mount_type)

    def __repr__(self):
        return 'BindMount[name={},mountType={}]'.format(self.name, self.mount_type.value)

    def __hash__(self):
        return hash((self.name, self.mount_type))

    @property
    def data(self):
        _data = super().data
        _mount_type = 'mountType'
        if _mount_type in _data.keys():
            raise TypeError('Implementation Error: Key \'{}\' already defined in parent class.'.format(_mount_type))
        _data[_mount_type] = self.mount_type.value
        return _data

    def state(self) -> PropertyState:
        _state = super().state()
        if isinstance(_state, PropertyUnavailable):
            return _state
        value = self.get_value()
        if not os.path.exists(value):
            return PropertyUnavailable('The value \'{}\' is not an existing path in the file system'.format(value))
        if not os.path.isfile(value) and self.mount_type == MountType.FILE:
            return PropertyUnavailable('The value \'{}\' is not a file, but it should be'.format(value))
        if not os.path.isdir(value) and self.mount_type == MountType.DIRECTORY:
            return PropertyUnavailable('The value \'{}\' is not a directory, but it should be'.format(value))
        return PROPERTY_AVAILABLE
