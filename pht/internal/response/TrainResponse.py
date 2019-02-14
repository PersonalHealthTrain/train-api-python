import abc
import json
from pht.internal.protocol.Typed import Typed


class TrainResponse(Typed, abc.ABC):
    """
    A TrainResponse is a document returned by the train in response to a train command
    """
    def as_json_string(self) -> str:
        return json.dumps(self.as_dict())
