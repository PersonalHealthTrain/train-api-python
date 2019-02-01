"""
Denotes the property of having an environment variable set

@author Lukas Zimmermann
"""
import abc
import os
import re
from typing import List
from .Property import Property


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
            'name': self.name,
            'check': self.check()
        }

    @property
    @abc.abstractmethod
    def target(self) -> str:
        pass

    def check(self) -> bool:
        return self.name in os.environ.keys()

    def get_value(self) -> str:
        return os.environ[self.name]

    def __str__(self):
        return self.__repr__()

    @abc.abstractmethod
    def __repr__(self):
        pass


class UrlEnvironmentVariableProperty(EnvironmentVariableProperty):

    def __init__(self, name):
        super().__init__(name)

    @property
    def target(self) -> str:
        return 'http://schema.org/URL'

    def __repr__(self):
        return 'Url[name={}]'.format(self.name)

    def copy(self):
        return UrlEnvironmentVariableProperty(self.name)


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


class EnumEnvironmentVariableProperty(EnvironmentVariableProperty):
    def __init__(self, name: str, choices: List[str]):
        super().__init__(name)
        self._validate_choices(choices)
        self._choices = frozenset(choices)

    @property
    def target(self) -> str:
        return 'enum'

    def copy(self):
        return EnumEnvironmentVariableProperty(self.name, [choice for choice in self._choices])

    def __repr__(self):
        return 'Enum[name={},choices={}]'.format(self.name, sorted(list(self._choices)))

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, EnumEnvironmentVariableProperty):
            return False
        return self.name == other.name and self._choices == other._choices

    def __hash__(self):
        return hash((self.name, self._choices))

    def check(self) -> bool:
        return super().check() and self.get_value() in self._choices

    def _validate_choices(self, choices: List[str]):
        if choices is None:
            raise ValueError('\'choices\' for enum environment variable cannot be None!')
        if not isinstance(choices, List):
            raise TypeError('\'choices\' for enum environment variable must be a List of str values')
        if len(choices) == 0:
            raise ValueError('List of choices for enum environment variable is not allowed to be empty')
        for choice in choices:
            if not isinstance(choice, str):
                raise ValueError('Value \'{}\' of \'choices\' is not a str'.format(str(choice)))
