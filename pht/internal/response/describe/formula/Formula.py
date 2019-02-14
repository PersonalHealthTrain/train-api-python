import abc
from pht.internal.protocol.Copyable import Copyable
from pht.internal.protocol.Comparable import Comparable
from pht.internal.protocol.Typed import Typed


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
