import abc
from pht.internal.protocol import Comparable, Copyable, Typed


class Formula(Typed, Comparable, Copyable):

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
