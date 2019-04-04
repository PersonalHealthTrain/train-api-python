"""
Contains the class: Formula
"""
from abc import abstractmethod
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass


class Formula(TypedAsPythonClass):
    """Represents a Formula"""

    @property
    def data(self) -> dict:
        """The data of this Formula"""
        return {
            'value': self.value
        }

    @property
    @abstractmethod
    def value(self):
        """
        Value of the Formula. The Type of the formula decides how this value actually looks like
        """
        pass
