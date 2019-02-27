import abc
import os
from functools import total_ordering
from pht.internal.protocol.Comparable import Comparable
from pht.internal.protocol.Typed import Typed


@total_ordering
class TrainFile(Comparable, Typed):

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

    @abc.abstractmethod
    def exists(self) -> bool:
        pass

    @staticmethod
    def base_dir():
        return os.path.join('/opt', 'pht_train')
