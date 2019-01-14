"""
Contains the abstract base class for a Property that a container can have.

@author Lukas Zimmermann
"""
import abc


class Property(abc.ABC):
    """
    Abstract base class for a property that can be formulated by a train.
    """
    @property
    @abc.abstractmethod
    def type(self) -> str:
        """
        The concept URI defined by this item.
        """
        pass

    @property
    @abc.abstractmethod
    def display(self) -> str:
        """
        The display name of this Property
        :return:
        """
        pass

    @abc.abstractmethod
    def to_dict(self) -> dict:
        """
        Dictionary representation of the property
        :return:
        """
        pass

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
