import abc
import contextlib
import os
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

    def __init__(self):
        self._keys = set()

    @staticmethod
    def _join_to_basedir(key: str):
        _basedir = '/opt/train'
        os.makedirs(_basedir, exist_ok=True)
        return os.path.join(_basedir, key)

    @abc.abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass

    @contextlib.contextmanager
    def trainfile(self, key: str, mode: str):
        self._keys.add(key)
        # Note: Cannot use with statement here, because using yield within a with-block is undefined behavior
        fd = open(AbstractTrain._join_to_basedir(key), mode)
        yield fd
        fd.close()

    def list_existing_trainfiles(self):
        return sorted([AbstractTrain._join_to_basedir(key) for key in self._keys if ])