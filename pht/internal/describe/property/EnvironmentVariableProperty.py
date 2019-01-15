"""
Denotes the property of having an environment variable set

@author Lukas Zimmermann
"""
from .Property import Property
import abc
import os
import re


_REGEX_ENVIRONMENT_VARIABLE = re.compile(r'^[A-Z]+(_[A-Z]+)*$')


def _is_valid_environment_variable(name: str) -> bool:
    return _REGEX_ENVIRONMENT_VARIABLE.fullmatch(name) is not None


class EnvironmentVariableProperty(Property):
    def __init__(self, name):
        self.name = name

        if self.name is None:
            raise ValueError('\'None\' is not allowed for the name of an Environment Variable')

        if not _is_valid_environment_variable(self.name):
            raise ValueError('Not a valid Environment variable: {}'.format(self.name))

    def __eq__(self, other):
        return isinstance(other, EnvironmentVariableProperty) \
               and self.name == other.name \
               and self.target == other.target

    def __hash__(self):
        return hash(self.type + self.target + self.name)

    @property
    def display(self) -> str:
        return 'environmentVariable'

    @property
    def type(self) -> str:
        return 'http://www.wikidata.org/entity/Q400857'

    @property
    def data(self) -> dict:
        return {
            'target': self.target,
            'name': self.name
        }

    @property
    @abc.abstractmethod
    def target(self) -> str:
        pass

    def check(self) -> bool:
        return self.name in os.environ.keys()


class UrlEnvironmentVariableProperty(EnvironmentVariableProperty):

    def __init__(self, name):
        super(UrlEnvironmentVariableProperty, self).__init__(name)

    @property
    def target(self) -> str:
        return 'http://schema.org/URL'

    def __repr__(self):
        return 'Url[name={}]'.format(self.name)

    def __str__(self):
        return self.__repr__()

    def copy(self):
        return UrlEnvironmentVariableProperty(self.name)
