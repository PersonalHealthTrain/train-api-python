"""
Contains the Command interface and the Abstract Train class
"""
import abc
import contextlib
import os
from pht.internal.station import StationRuntimeInfo
from pht.internal.describe import TrainDescription
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
    def _join_to_basedir(key: str) -> str:
        _basedir = '/opt/train'
        os.makedirs(_basedir, exist_ok=True)
        return os.path.join(_basedir, key)

    @staticmethod
    def _is_valid_trainfile(filename):
        """
        For a trainfile to be valid, the following conditions need to be met:
        1. The filepath needs to be absolute
        2. The file must be regular
        3. The file must not be a link
        :param filename: File to be checked
        :return: Whether the filename refers to a valid trainfile
        """
        return os.path.isfile(filename) and os.path.isabs(filename) and not os.path.islink(filename)

    @abc.abstractmethod
    def describe(self, info: StationRuntimeInfo) -> TrainDescription:
        pass

    @abc.abstractmethod
    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass

    @contextlib.contextmanager
    def trainfile(self, key: str, mode: str):
        forbidden = '/'
        if forbidden in key:
            raise ValueError("The character \'{}\' is not allowed to be part of the key!".format(forbidden))
        self._keys.add(key)
        # Note: Cannot use with statement here, because using yield within a with-block is undefined behavior
        fd = open(AbstractTrain._join_to_basedir(key), mode)
        yield fd
        fd.close()

    def list_existing_trainfiles(self):
        res = []
        for key in self._keys:
            filename = AbstractTrain._join_to_basedir(key)
            if AbstractTrain._is_valid_trainfile(filename):
                res.append(filename)
        return sorted(res)
