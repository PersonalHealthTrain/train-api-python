"""
Defines the operations that a train class needs to support
"""
from abc import ABC, abstractmethod
from pht.internal.response.run import RunResponse
from pht.internal.response.describe import TrainDescription
from .StationRuntimeInfo import StationRuntimeInfo


class TrainCommandInterface(ABC):
    """Defines the operations that a train class needs to support"""
    @abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        """
        Asks the train to describe itself. This will return the Train Description of the Train
        """
        pass

    @abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        """
        Asks the train to execute the encapsulated algorithm. Returns the RunResponse
        """
        pass
