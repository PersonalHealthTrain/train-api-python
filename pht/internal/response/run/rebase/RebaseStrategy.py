"""
Base class for a rebase strategy
"""
import abc
import re
from typing import List
from pht.internal.protocol.Typed import Typed
from pht.internal.protocol.Copyable import Copyable
from pht.internal.protocol.Comparable import Comparable
from pht.internal.train.cargo.TrainFile import TrainFile


_TRAIN_TAG_REGEX = re.compile(r'^[-.a-z0-9]+$')


class IllegalResponseException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def _train_tag_is_valid(value: str):
    return _TRAIN_TAG_REGEX.fullmatch(value) is not None


class RebaseStrategy(Copyable, Comparable, Typed, abc.ABC):
    def __init__(self,
                 next_train_tags: List[str],
                 export_files: List[TrainFile]):

        RebaseStrategy._validate_next_train_tags(next_train_tags)
        self.next_train_tags = frozenset(next_train_tags)
        self.export_files = frozenset(export_files)

    @property
    def data(self) -> dict:
        return {
            'exportFiles': [x.as_simple_dict() for x in sorted(list(self.export_files))],
            'nextTrainTags': sorted(list(self.next_train_tags))
        }

    @staticmethod
    def _validate_next_train_tags(tags: List[str]):
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
        return self.type_name

    @property
    def type_name(self) -> str:
        return 'docker'

    @property
    def data(self) -> dict:
        result = super().data
        result['from'] = self.frm
        return result

    def __eq__(self, other):
        return other is self or \
               (isinstance(other, DockerRebaseStrategy) and self.frm == other.frm and
                self.next_train_tags == other.next_train_tags and self.export_files == other.export_files)

    def __hash__(self):
        return hash((self.frm, self.next_train_tags, self.export_files))

    def copy(self):
        return DockerRebaseStrategy(self.frm, list(self.next_train_tags), list(self.export_files))
