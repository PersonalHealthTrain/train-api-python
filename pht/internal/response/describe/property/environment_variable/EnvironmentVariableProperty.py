from abc import abstractmethod
import os
import re
from typing import Optional
from ..Property import Property
from ..PropertyState import PropertyState
from pht.internal.util import require

_REGEX_ENVIRONMENT_VARIABLE = re.compile(r'^[A-Z]+(_[A-Z]+)*$')


def _is_valid_environment_variable(name: str) -> bool:
    return _REGEX_ENVIRONMENT_VARIABLE.fullmatch(name) is not None


class EnvironmentVariableProperty(Property):
    """A Property Representing an environment variable"""
    def __init__(self, name: str, description: Optional[str] = None):
        self.name = name
        self.description = '' if description is None else description
        require.type_is_str(self.name)

        if not _is_valid_environment_variable(self.name):
            raise ValueError('Not a valid Environment variable: {}'.format(self.name))

    def __hash__(self):
        return hash((tuple(self.type), self.name))

    @property
    def data(self) -> dict:
        return {
            'description': self.description,
            'environmentVariableName': self.name,
            'state': self.state().as_simple_mapping()
        }

    def state(self) -> PropertyState:
        """An EnvironmentVariable is satisfied if the name exists in the environment and the value does not only consist
        of whitespace"""
        def _is_only_whitespace(text: str):
            return len(text.strip()) < 1
        if self.name in os.environ.keys() and not _is_only_whitespace(os.environ[self.name]):
            return PropertyState(is_satisfied=True)
        return PropertyState(
            is_satisfied=False,
            reason='Environment variable \'{}\' not set'.format(self.name))

    def get_value(self) -> str:
        """Returns the value of the environment variable or key error if its not present"""
        return os.environ[self.name]

    def __str__(self):
        return self.__repr__()

    @abstractmethod
    def __repr__(self):
        pass
