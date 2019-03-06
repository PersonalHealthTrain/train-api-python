import abc
import os
import re
from typing import Optional
from ..Property import Property
from ..PropertyState import PropertyState, PropertyUnavailable, PROPERTY_AVAILABLE


_REGEX_ENVIRONMENT_VARIABLE = re.compile(r'^[A-Z]+(_[A-Z]+)*$')


def _is_valid_environment_variable(name: str) -> bool:
    return _REGEX_ENVIRONMENT_VARIABLE.fullmatch(name) is not None


class EnvironmentVariableProperty(Property):
    def __init__(self, name: str, description: Optional[str] = None):
        self.name = name
        self.description = '' if description is None else description

        if self.name is None:
            raise ValueError('\'None\' is not allowed for the name of an Environment Variable')

        if not _is_valid_environment_variable(self.name):
            raise ValueError('Not a valid Environment variable: {}'.format(self.name))

    def __hash__(self):
        return hash((self.type, self.name))

    @property
    def data(self) -> dict:
        return {
            'description': self.description,
            'environmentVariableName': self.name,
            'state': self.state().as_simple_dict()
        }

    def state(self) -> PropertyState:
        if self.name in os.environ.keys():
            return PROPERTY_AVAILABLE
        return PropertyUnavailable('Environment variable \'{}\' not set'.format(self.name))

    def get_value(self) -> str:
        return os.environ[self.name]

    def __str__(self):
        return self.__repr__()

    @abc.abstractmethod
    def __repr__(self):
        pass
