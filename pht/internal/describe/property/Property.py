"""
Contains the abstract base class for a Property that a container can have.

@author Lukas Zimmermann
"""
import abc
from pht.internal import Typed


class Property(Typed):
    """
    Abstract base class for a property that can be formulated by a train.
    """
    @abc.abstractmethod
    def check(self) -> bool:
        """
        Checks whether the Property denotes by this object is met in the environment
        :return: Whether this Property is met in the environment
        """
        pass

    @abc.abstractmethod
    def copy(self):
        pass

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()

    @abc.abstractmethod
    def __eq__(self, other):
        pass
