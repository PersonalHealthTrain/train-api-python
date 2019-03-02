import abc
import os
import re
from ..Property import Property
from ..PropertyState import PropertyState, PropertyUnavailable, PROPERTY_AVAILABLE


_REGEX_ENVIRONMENT_VARIABLE = re.compile(r'^[A-Z]+(_[A-Z]+)*$')


def _is_valid_environment_variable(name: str) -> bool:
    return _REGEX_ENVIRONMENT_VARIABLE.fullmatch(name) is not None


class EnvironmentVariableProperty(Property):
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description

        if self.name is None:
            raise ValueError('\'None\' is not allowed for the name of an Environment Variable')

        if not _is_valid_environment_variable(self.name):
            raise ValueError('Not a valid Environment variable: {}'.format(self.name))

    def __eq__(self, other):
        return isinstance(other, EnvironmentVariableProperty) \
               and self.name == other.name \
               and self.target == other.target

    def __hash__(self):
        return hash((self.type, self.target, self.name))

    @property
    def type_name(self) -> str:
        return 'environmentVariable'

    @property
    def type(self) -> str:
        return 'http://www.wikidata.org/entity/Q400857'

    @property
    def data(self) -> dict:
        return {
            'description': self.description,
            'target': self.target,
            'name': self.name,
            'state': self.state().as_dict()
        }

    @property
    @abc.abstractmethod
    def target(self) -> str:
        pass

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
