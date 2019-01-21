import abc
from .station import StationRuntimeInfo
from .describe import TrainDescription
from pht.train.response import RunResponse


class AbstractTrain(abc.ABC):

    @abc.abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass
