import os
from functools import total_ordering
from .TrainFile import TrainFile


@total_ordering
class AlgorithmFile(TrainFile):
    def __init__(self, file_name: str):
        self._path = os.path.join(AlgorithmFile.base_dir(), file_name)

    @property
    def absolute_path(self) -> str:
        return self._path

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'AlgorithmFile'

    @staticmethod
    def base_dir():
        return os.path.join(TrainFile.base_dir(), 'algorithm')

    @staticmethod
    def list():
        def _is_allowed(filename):
            return not any([filename.endswith(x) for x in ['pyc']])
        return [AlgorithmFile(filename)
                for folder, _, files in os.walk(AlgorithmFile.base_dir())
                for filename in files if _is_allowed(filename)]
