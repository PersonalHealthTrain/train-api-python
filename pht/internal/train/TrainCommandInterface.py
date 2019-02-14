import abc
from pht.internal.response.run import RunResponse
from pht.internal.response.describe import TrainDescription
from .StationRuntimeInfo import StationRuntimeInfo


class TrainCommandInterface(abc.ABC):

    @abc.abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass
