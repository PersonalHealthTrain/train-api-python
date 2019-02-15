from .EnvironmentVariableProperty import EnvironmentVariableProperty


class UrlEnvironmentVariableProperty(EnvironmentVariableProperty):

    @property
    def target(self) -> str:
        return 'http://schema.org/URL'

    def __repr__(self):
        return 'Url[name={}]'.format(self.name)

    def copy(self):
        return UrlEnvironmentVariableProperty(self.name, self.description)
