import abc
import os
from functools import total_ordering
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass


@total_ordering
class TrainFile(TypedAsPythonClass):

    @property
    @abc.abstractmethod
    def absolute_path(self) -> str:
        pass

    def __eq__(self, other):
        return self is other or \
               (isinstance(other, TrainFile) and self.absolute_path == other.absolute_path)

    def __hash__(self):
        return hash(self.absolute_path)

    def __lt__(self, other):
        return self.absolute_path < other.absolute_path

    @property
    def data(self) -> dict:
        return {
            'absolutePath': self.absolute_path
        }

    def exists(self) -> bool:
        return os.path.isfile(self.absolute_path)

    @staticmethod
    def base_dir():
        return os.path.join('/opt', 'pht_train')
