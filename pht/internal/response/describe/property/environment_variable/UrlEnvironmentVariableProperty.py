"""
Contains the UrlEnvironmentVariableProperty class
"""
from .EnvironmentVariableProperty import EnvironmentVariableProperty


class UrlEnvironmentVariableProperty(EnvironmentVariableProperty):
    """An UrlEnvironmentVariableProperty contains an URL as value"""
    def __repr__(self):
        return 'Url[name={}]'.format(self.name)

    def deepcopy(self):
        """Returns a Deep Copy of this UrlEnvironmentVariableProperty"""
        return UrlEnvironmentVariableProperty(self.name, self.description)
