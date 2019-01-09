"""
Contains the abstract base class for a Requirement that can be formulated by a train.

@author Lukas Zimmermann
"""
from abc import ABC, abstractmethod


class Requirement(ABC):
    """
    Abstract base class for a requirement that can be formulated by a train.
    """

    @property
    @abstractmethod
    def type(self) -> str:
        """
        Gives the str representation of the requirement that this class reflects
        :return: The str representation of the requirement type
        """
        pass

    @abstractmethod
    def to_dict(self):
        """
        Dictionary representation of the requirement
        :return:
        """
        pass
