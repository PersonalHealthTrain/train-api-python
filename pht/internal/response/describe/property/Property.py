"""
Contains the abstract base class for a Property that a container can have.
"""
from abc import abstractmethod
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass
from pht.internal.response.describe.property.PropertyState import PropertyState


class Property(TypedAsPythonClass):
    """Abstract base class for a property that can be formulated by a train."""
    @abstractmethod
    def state(self) -> PropertyState:
        """Returns the State of the Property"""
        pass
