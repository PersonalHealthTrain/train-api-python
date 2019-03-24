from .EnvironmentVariableProperty import EnvironmentVariableProperty


class UrlEnvironmentVariableProperty(EnvironmentVariableProperty):

    def __repr__(self):
        return 'Url[name={}]'.format(self.name)

    def deepcopy(self):
        return UrlEnvironmentVariableProperty(self.name, self.description)
