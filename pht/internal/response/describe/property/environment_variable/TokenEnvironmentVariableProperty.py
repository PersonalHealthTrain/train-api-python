from .EnvironmentVariableProperty import EnvironmentVariableProperty


class TokenEnvironmentVariableProperty(EnvironmentVariableProperty):

    def __repr__(self):
        return 'Token[name={}]'.format(self.name)

    def deepcopy(self):
        return TokenEnvironmentVariableProperty(self.name, self.description)
