import abc
import os
from typing import List
from pht.internal.train.cargo.AlgorithmFile import AlgorithmFile
from pht.internal.train.cargo.ModelFile import ModelFile
from pht.internal.train.cargo.ModelFile import TrainFile
from .TrainCommandInterface import TrainCommandInterface


class AbstractTrain(TrainCommandInterface, abc.ABC):
    """
    Train with support for trainfiles
    """
    def __init__(self):
        self._model_files = {}

        # Directories for the train cargo are created upon Train instantiation
        os.makedirs(AlgorithmFile.base_dir(), exist_ok=True)
        os.makedirs(ModelFile.base_dir(), exist_ok=True)

    def model_file(self, key: str) -> ModelFile:
        if key not in self._model_files.keys():
            self._model_files[key] = ModelFile(key)
        return self._model_files[key]

    def export_files(self) -> List[TrainFile]:
        """
        Lists all the files that this Abstract Train should export.
        """
        existing_model_files = [model_file for model_file in self._model_files.values() if model_file.exists()]
        algorithm_files = AlgorithmFile.list()
        return sorted(existing_model_files + algorithm_files)
