import abc
from typing import Optional
from .station import StationRuntimeInfo
from .describe import TrainDescription
from pht.train.response import RunResponse


class TrainCommandInterface(abc.ABC):

    @abc.abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass


class AbstractTrain(TrainCommandInterface):

    @abc.abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass

    def put_value_to_filesystem(self, key: str, value, hint: Optional[str] = None):
        pass

    def get_value_from_filesystem(self, key: str):
        pass
