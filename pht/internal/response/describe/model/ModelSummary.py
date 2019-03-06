import abc
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass
from pht.internal.protocol.Copyable import Copyable


class ModelSummary(TypedAsPythonClass, Copyable, abc.ABC):

    @property
    def data(self) -> dict:
        return {
            'value': self.value
        }

    @property
    @abc.abstractmethod
    def value(self):
        """
        Value of the Model Summary. The Type of the Model Summary defines the type of the value
        """
        pass
