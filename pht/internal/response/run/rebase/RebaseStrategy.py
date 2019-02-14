"""
Base class for a rebase strategy
"""
import abc
import re
import os
from typing import List
from pht.internal.protocol.Typed import Typed
from pht.internal.train.TrainFile import TrainFile

_TRAIN_TAG_REGEX = re.compile(r'^[-.a-z0-9]+$')


class IllegalResponseException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def _train_tag_is_valid(value: str):
    return _TRAIN_TAG_REGEX.fullmatch(value) is not None


def _file_is_valid(p: str) -> bool:
    """
    Checks that the file referenced by the path is an existing regular file and not a symlink. Also, the
    path needs to be absolute.
    :param path: The path to be tested
    :return: Whether the path is valid as defined above
    """
    return os.path.isabs(p) and os.path.isfile(p) and not os.path.islink(p)


class RebaseStrategy(Typed):
    def __init__(self,
                 next_train_tags: List[str],
                 export_files: List[TrainFile]):

        self._validate_next_train_tags(next_train_tags)
        self.next_train_tags = frozenset(next_train_tags)
        self.export_files = frozenset(export_files)

    @property
    def data(self) -> dict:
        return {
            'export_files': sorted(list(self.export_files)),
            'next_train_tags': sorted(list(self.next_train_tags))
        }

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass

    def copy(self):
        pass

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()

    def _validate_next_train_tags(self, tags: List[str]):
        if tags is None:
            raise ValueError('\'tags\' for Rebase Strategy is not allowed be None')
        if not isinstance(tags, List):
            raise TypeError('\'tags\' for Rebase Strategy must be a List of str values')
        for tag in tags:
            if not isinstance(tag, str):
                raise ValueError('Tag \'{}\' of \'tag\' is not a str'.format(str(tag)))
            if not _train_tag_is_valid(tag):
                raise IllegalResponseException('Next train tag {} is invalid!'.format(tag))


class DockerRebaseStrategy(RebaseStrategy):

    def __init__(self,
                 frm: str,
                 next_train_tags: List[str],
                 export_files: List[TrainFile]):
        super().__init__(next_train_tags, export_files)
        self.frm = frm

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'docker'

    @property
    def data(self) -> dict:
        result = super().data
        result['from'] = self.frm
        return result

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, DockerRebaseStrategy):
            return False
        return self.frm == other.frm and self.next_train_tags == other.next_train_tags and self.export_files == other.export_files

    def __hash__(self):
        return hash((self.frm, self.next_train_tags, self.export_files))

    def copy(self):
        return DockerRebaseStrategy(self.frm, list(self.next_train_tags), list(self.export_files))
