"""
Contains the class: TrainResponse
"""
import json
from abc import ABC
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass
from pht.internal.util.typetest import is_mapping, is_list, is_primitive


class TrainResponse(TypedAsPythonClass, ABC):
    """
    A TrainResponse is a document returned by the train in response to a train command
    """
    def as_json_string(self) -> str:
        """
        Returns the JSON-encoded String of the Train Response
        """
        def _to_dict(value):
            if is_primitive(value):
                return value
            if is_list(value):
                return [_to_dict(x) for x in value]
            if is_mapping(value):
                return {key: _to_dict(value) for key, value in value.items()}
        # Conversion to dictionary necessary since Mapping (mappingproxy) is not generally JSON serializable
        return json.dumps(_to_dict(self.as_simple_mapping()),
                          separators=(',', ':'),
                          allow_nan=False)
