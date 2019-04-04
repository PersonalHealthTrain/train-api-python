"""
Contains the class: ModelSummary
"""
from abc import ABC, abstractmethod
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass
from pht.internal.protocol.DeepCopyable import DeepCopyable


class ModelSummary(TypedAsPythonClass, DeepCopyable, ABC):
    """Represents the summary of the current Model of the Train"""
    @property
    def data(self) -> dict:
        """The data of the model"""
        return {
            'value': self.value
        }

    @property
    @abstractmethod
    def value(self):
        """Value of the Model Summary. The Type of the Model Summary defines the type of the value"""
        pass
