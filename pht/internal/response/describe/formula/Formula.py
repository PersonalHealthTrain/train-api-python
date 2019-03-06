import abc
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass


class Formula(TypedAsPythonClass):

    @property
    def data(self) -> dict:
        return {
            'value': self.value
        }

    @property
    @abc.abstractmethod
    def value(self):
        """
        Value of the Formula. The Type of the formula decides how this value actually looks like
        """
        pass
