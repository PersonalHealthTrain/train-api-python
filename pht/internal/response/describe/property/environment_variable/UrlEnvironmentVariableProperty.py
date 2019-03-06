from .EnvironmentVariableProperty import EnvironmentVariableProperty


class UrlEnvironmentVariableProperty(EnvironmentVariableProperty):

    def __repr__(self):
        return 'Url[name={}]'.format(self.name)

    def copy(self):
        return UrlEnvironmentVariableProperty(self.name, self.description)
