"""
Contains the abstract base class for a Property that a container can have.

@author Lukas Zimmermann
"""
import abc
from pht.internal.protocol import Comparable, Copyable, Typed
from pht.internal.response.describe.property.PropertyState import PROPERTY_AVAILABLE, PropertyState


class Property(Typed, Copyable, Comparable):
    """
    Abstract base class for a property that can be formulated by a train.
    """
    @abc.abstractmethod
    def state(self) -> PropertyState:
        """
        Checks whether the Property denotes by this object is met in the environment
        :return: Whether this Property is met in the environment
        """
        pass

    def is_available(self) -> bool:
        return self.state() == PROPERTY_AVAILABLE
