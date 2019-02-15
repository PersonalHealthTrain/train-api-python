from .EnvironmentVariableProperty import EnvironmentVariableProperty


class TokenEnvironmentVariableProperty(EnvironmentVariableProperty):

    @property
    def target(self) -> str:
        return 'token'

    def __repr__(self):
        return 'Token[name={}]'.format(self.name)

    def copy(self):
        return TokenEnvironmentVariableProperty(self.name, self.description)
