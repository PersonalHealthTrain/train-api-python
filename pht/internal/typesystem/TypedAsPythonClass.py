import abc
from pht.internal.typesystem.Typed import Typed


class TypedAsPythonClass(Typed, abc.ABC):
    """
    Implements the Python class type system. This implies that type and type_name property are identical and
    equal the class name of the respective Python class
    """

    @property
    def type(self) -> str:
        return self.type_name

    @property
    def type_name(self) -> str:
        return self.__class__.__name__

    @property
    def type_system(self) -> str:
        return 'pythonclass'
