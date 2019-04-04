"""
Contains the class: TrainResponse
"""
import json
from abc import ABC
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass


class TrainResponse(TypedAsPythonClass, ABC):
    """
    A TrainResponse is a document returned by the train in response to a train command
    """
    def as_json_string(self) -> str:
        """
        Returns the JSON-encoded String of the Train Response
        """
        return json.dumps(self.as_simple_mapping(), separators=(',', ':'), allow_nan=False)
