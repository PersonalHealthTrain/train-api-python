"""
Contains the TrainFile Base class
"""
from abc import abstractmethod
from collections.abc import Hashable
from functools import total_ordering
import os
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass


@total_ordering
class TrainFile(Hashable, TypedAsPythonClass):
    """A TrainFile is a file in a file system that belongs to a train"""

    @property
    @abstractmethod
    def absolute_physical_path(self) -> str:
        """The absolute, physical path to this train file"""
        pass

    def __hash__(self):
        return hash(self.absolute_physical_path)

    def __lt__(self, other):
        return self.absolute_physical_path < other.absolute_physical_path

    @property
    def data(self) -> dict:
        """The data of a Train File"""
        return {
            'absolutePhysicalPath': self.absolute_physical_path
        }

    def exists(self) -> bool:
        """Checks whether the TrainFile is a regular file and not a link"""
        return os.path.isfile(self.absolute_physical_path) and not os.path.islink(self.absolute_physical_path)

    @staticmethod
    def base_dir():
        """
        Where train files are stored in the File System
        """
        return os.path.join('/opt', 'pht_train')
