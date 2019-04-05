"""
Contains the class TokenEnvironmentVariableProperty
"""
from .EnvironmentVariableProperty import EnvironmentVariableProperty


class TokenEnvironmentVariableProperty(EnvironmentVariableProperty):
    """A TokenEnvironmentVariable contains a fixed String as value"""

    def __repr__(self):
        return 'Token[name={}]'.format(self.name)

    def deepcopy(self):
        """Returns a Deep Copy of this TokenEnvironmentVariableProperty"""
        return TokenEnvironmentVariableProperty(self.name, self.description)
