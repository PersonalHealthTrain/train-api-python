import abc
import os
from typing import List
from pht.internal.train.cargo.AlgorithmFile import AlgorithmFile
from pht.internal.train.cargo.ModelFile import ModelFile
from .TrainCommandInterface import TrainCommandInterface


class AbstractTrain(TrainCommandInterface, abc.ABC):
    """
    Train with support for trainfiles
    """
    def __init__(self):
        self._model_files = set()

        # Directories for the train cargo are created upon Train instantiation
        os.makedirs(AlgorithmFile.base_dir(), exist_ok=True)
        os.makedirs(ModelFile.base_dir(), exist_ok=True)

    def model_file(self, key: str):
        _model_file = ModelFile(key)
        self._model_files.add(_model_file)
        return _model_file

    def export_files(self) -> List[str]:
        existing_model_files = [model_file for model_file in self._model_files if model_file.exists()]
        algorithm_files = AlgorithmFile.list()
        return sorted(existing_model_files + algorithm_files)
