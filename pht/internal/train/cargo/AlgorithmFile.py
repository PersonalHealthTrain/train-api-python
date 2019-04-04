import os
from functools import total_ordering
from .TrainFile import TrainFile
from pht.internal.util import require


@total_ordering
class AlgorithmFile(TrainFile):
    """A file that contains a part of the algorithm that the train realizes."""
    def __init__(self, file_name: str):
        self._file_name = file_name
        require.type_is_str(self._file_name)

    @property
    def absolute_physical_path(self) -> str:
        """The absolute physical file path of the algorithm file"""
        return os.path.join(AlgorithmFile.base_dir(), self._file_name)

    def deepcopy(self):
        """Returns a Deep Copy of the Algorithm File"""
        return AlgorithmFile(self._file_name)

    @staticmethod
    def base_dir():
        """Where train algorithm files are located on the file system"""
        return os.path.join(TrainFile.base_dir(), 'algorithm')

    @staticmethod
    def list():
        """Recursive list all algorithm files found inside the file system"""
        def _is_allowed(filename):
            return not any(filename.endswith(x) for x in {'pyc'})
        return [AlgorithmFile(filename)
                for folder, _, files in os.walk(AlgorithmFile.base_dir())
                for filename in files if _is_allowed(filename)]
