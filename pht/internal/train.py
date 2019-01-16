import abc
from pht.internal import RunResponse, TrainDescription


class AbstractTrain(abc.ABC):

    @abc.abstractmethod
    def describe(self) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self) -> RunResponse:
        pass
