from typing import List
from .EnvironmentVariableProperty import EnvironmentVariableProperty
from ..PropertyState import PropertyState, PropertyUnavailable, PROPERTY_AVAILABLE


class EnumEnvironmentVariableProperty(EnvironmentVariableProperty):
    def __init__(self, name: str, choices: List[str]):
        super().__init__(name)
        self._validate_choices(choices)
        self._choices = frozenset(choices)

    @property
    def target(self) -> str:
        return 'enum'

    @property
    def data(self) -> dict:
        _data = super().data
        _data['choices'] = sorted(list(self._choices))
        return _data

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

    def state(self) -> PropertyState:
        _state = super().state()
        if isinstance(super().state(), PropertyUnavailable):
            return _state
        value = self.get_value()
        if self.get_value() not in self._choices:
            return PropertyUnavailable('The value {} is not one of the allowed choices!'.format(value))
        return PROPERTY_AVAILABLE

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
