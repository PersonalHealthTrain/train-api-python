"""
The TypeSystem that uses the Python class Name
"""
import abc
from typing import List
from pht.internal.typesystem.Typed import Typed
from pht.internal.typesystem.TypeSystem import TypeSystem


class TypedAsPythonClass(Typed, abc.ABC):
    """
    Implements the Python class type system. This implies that type and type_name property are identical and
    equal the class name of the respective Python class
    """

    @property
    def type(self) -> List[str]:
        """The Type"""
        return TypedAsPythonClass.parents_types(self)

    @property
    def type_name(self) -> str:
        """The Name of the Type"""
        return self.__class__.__name__

    @property
    def type_system(self) -> TypeSystem:
        """The Type System"""
        return TypeSystem('pythonclass', '1.0')

    @staticmethod
    def parents_types(obj):
        """Determines all Patent types of the provided object"""
        result = []

        def search(clz):
            clz_name = clz.__name__
            # Too far
            if clz_name == 'type':
                return False
            elif clz_name == 'TypedAsPythonClass':
                return True
            result.append(clz_name)
            for base in clz.__bases__:
                if search(base):
                    return True
            result.pop()
            return False
        if not search(obj.__class__):
            raise AssertionError('Try to find Parent typed for class that does not derive from TypedAsPythonClass')
        return result
