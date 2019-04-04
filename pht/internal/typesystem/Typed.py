"""
Contains the 'Typed' interface.

An object which is 'typed' has a 'type' property that is associated with a certain Type System
"""

from abc import abstractmethod
from typing import List, Union
from pht.internal.util import require
from pht.internal.util.predicate.maker import not_in
from pht.internal.protocol.SimpleMappingRepresentable import SimpleMappingRepresentable
from pht.internal.protocol.DeepCopyable import DeepCopyable
from pht.internal.typesystem.TypeSystem import TypeSystem


class Typed(DeepCopyable, SimpleMappingRepresentable):
    """Classes that are Typed have a type and type_name property that is associated with a certain type system"""
    @property
    @abstractmethod
    def type(self) -> Union[str, List[str]]:
        """The type of the class"""
        pass

    @property
    @abstractmethod
    def type_name(self) -> str:
        """The type name of the type"""
        pass

    @property
    @abstractmethod
    def type_system(self) -> TypeSystem:
        """The type system of the type"""
        pass

    @property
    @abstractmethod
    def data(self) -> dict:
        """The data for the type used to implement the SimpleMapping Representable interface"""
        pass

    def _as_dict(self) -> dict:
        # Meta Keys for the Type
        _type = '@type'
        _typeName = '@typeName'
        _typeSystem = '@typeSystem'

        data = self.data
        require.for_each_value(
            inside=[_type, _typeName, _typeSystem],
            that=not_in(data.keys()),
            error_if_not='Key \'{}\' not allowed in data dictionary of class')
        data.update({
            _type: self.type,
            _typeName: self.type_name,
            _typeSystem: self.type_system.as_simple_mapping()
        })
        return data
