import abc
from pht.internal.describe import TrainDescription


class AbstractTrain(abc.ABC):

    @abc.abstractmethod
    def describe(self) -> TrainDescription:
        pass



