import abc
from pht.internal import StationRuntimeInfo, TrainDescription
from pht.response import RunResponse


class AbstractTrain(abc.ABC):

    @abc.abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass
