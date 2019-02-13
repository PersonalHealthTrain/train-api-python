from .EnvironmentVariableProperty import EnvironmentVariableProperty


class TokenEnvironmentVariableProperty(EnvironmentVariableProperty):
    def __init__(self, name):
        super().__init__(name)

    @property
    def target(self) -> str:
        return 'token'

    def __repr__(self):
        return 'Token[name={}]'.format(self.name)

    def copy(self):
        return TokenEnvironmentVariableProperty(self.name)
