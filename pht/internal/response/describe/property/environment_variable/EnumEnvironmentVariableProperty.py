"""
Contains the class: EnumEnvironmentVariableProperty
"""
from typing import Optional, List
from .EnvironmentVariableProperty import EnvironmentVariableProperty
from ..PropertyState import PropertyState


class EnumEnvironmentVariableProperty(EnvironmentVariableProperty):
    """An environment variable where the values must come from a fixed value set"""
    def __init__(self, name: str, description: Optional[str], choices: List[str]):
        super().__init__(name, description)
        self._validate_choices(choices)
        self._choices = frozenset(choices)

    @property
    def data(self) -> dict:
        """The data of the EnumEnvironmentVariableProperty"""
        _data = super().data
        _choices = 'choices'
        if _choices in _data.keys():
            raise TypeError('Implementation Error: Key \'{}\' already defined in parent class'.format(_choices))
        _data[_choices] = sorted(list(self._choices))
        return _data

    def deepcopy(self):
        """Returns a Deep Copy of this Enum Environment Variable"""
        return EnumEnvironmentVariableProperty(self.name, self.description, [choice for choice in self._choices])

    def __repr__(self):
        return 'Enum[name={},choices={}]'.format(self.name, sorted(list(self._choices)))

    def __hash__(self):
        return hash((self.name, self._choices))

    def state(self) -> PropertyState:
        """An EnumEnvironmentVariable is satisfied if the value in the environment comes from a fixed value set"""
        _state = super().state()
        if not _state.is_satisfied:
            return _state
        value = self.get_value()
        if value not in self._choices:
            return PropertyState(
                is_satisfied=False,
                reason='The value {} is not one of the allowed choices!'.format(value))
        return PropertyState(is_satisfied=True)

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
