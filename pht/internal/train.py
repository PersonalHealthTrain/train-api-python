import abc
from pht.internal import TrainDescription
from pht.response import RunResponse


class AbstractTrain(abc.ABC):

    @abc.abstractmethod
    def describe(self) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self) -> RunResponse:
        pass
