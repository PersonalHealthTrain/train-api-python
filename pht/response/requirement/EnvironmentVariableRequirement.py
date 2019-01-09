"""
Denotes the requirement of having an environment variable set

@author Lukas Zimmermann
"""
from .Requirement import Requirement
from typing import Pattern, Callable
import re
from abc import abstractmethod

# A String Checker is a function that checks whether a string fullfills a certain condition
StringChecker = Callable[[str], bool]


def _string_checker_for(regex: Pattern[str]) -> StringChecker:
    """
    Creates a function that checks whether the provided pattern matches the given input String of the function
    :param regex:
    :return:
    """
    def _result(string: str) -> bool:
        return regex.match(string) is not None
    return _result


_is_environment_variable: StringChecker = _string_checker_for(re.compile(r'^[A-Z]+(_[A-Z]+)*$'))


class EnvironmentVariableRequirement(Requirement):
    def __init__(self, name):
        self.name = name
        if not _is_environment_variable(self.name):
            raise ValueError('Not a valid Environment variable: {}'.format(self.name))

    def __eq__(self, other):
        return isinstance(other, EnvironmentVariableRequirement) \
               and self.name == other.name \
               and self.target == other.target

    def __hash__(self):
        return hash(self.type + self.target + self.name)

    @property
    def type(self) -> str:
        return 'environmentVariable'

    def to_dict(self):
        return {
            'type': self.type,
            'target': self.target,
            'name': self.name
        }

    @property
    @abstractmethod
    def target(self) -> str:
        pass


class URLEnvironmentVariableRequirement(EnvironmentVariableRequirement):

    def __init__(self, name):
        super(URLEnvironmentVariableRequirement, self).__init__(name)

    @property
    def target(self) -> str:
        return 'URL'


def req_url(name: str) -> Requirement:
    """
    Shortcut for creating an URL as an requirement
    :param name: The name of the environment variable
    :return: The corresponding Requirement instance
    """
    return URLEnvironmentVariableRequirement(name)
