import abc
from pht.internal import Typed


class Formula(Typed):

    @property
    def data(self) -> dict:
        return {
            'value': self.value()
        }

    @abc.abstractmethod
    def value(self):
        """
        Value of the Formula
        """
        pass
