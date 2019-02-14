import abc
import os
from typing import List
from pht.internal.train.TrainFile import TrainFile
from .TrainCommandInterface import TrainCommandInterface


class AbstractTrain(TrainCommandInterface, abc.ABC):

    def __init__(self):
        self._trainfiles = set()

    def trainfile(self, key: str):
        trainfile = TrainFile(key)
        self._trainfiles.add(trainfile)
        return trainfile

    def list_existing_trainfiles(self) -> List[TrainFile]:
        return sorted([trainfile for trainfile in self._trainfiles if os.path.isfile(trainfile.path)])
