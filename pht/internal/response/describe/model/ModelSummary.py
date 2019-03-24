import abc
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass
from pht.internal.protocol.DeepCopyable import DeepCopyable


class ModelSummary(TypedAsPythonClass, DeepCopyable, abc.ABC):

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
