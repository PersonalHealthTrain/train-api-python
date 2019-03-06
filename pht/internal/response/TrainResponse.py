import abc
import json
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass


class TrainResponse(TypedAsPythonClass, abc.ABC):
    """
    A TrainResponse is a document returned by the train in response to a train command
    """
    def as_json_string(self) -> str:
        return json.dumps(self.as_simple_dict(), separators=(',', ':'))
