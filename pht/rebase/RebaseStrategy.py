"""
Base class for a rebase strategy
"""
import abc
import re
import os
from typing import List, Union
from pathlib import Path
from pht.internal import IllegalResponseException, Typed

_TRAIN_TAG_REGEX = re.compile(r'^[-.a-z0-9]+$')

# Anything that can represent a Path
PathThing = Union[str, Path, os.PathLike]


def _train_tag_is_valid(value: str):
    return _TRAIN_TAG_REGEX.fullmatch(value) is not None


def _file_is_valid(p: str) -> bool:
    """
    Checks that the file referenced by the path is an existing regular file and not a symlink. Also, the
    path needs to be absolute.
    :param path: The path to be tested
    :return: Whether the path is valid as defined above
    """
    path = os.path
    return path.isabs(p) and path.isfile(p) and not path.islink(p)


def _normalize_paths(paths: List[PathThing]) -> List[str]:
    """
    Converts several path Types to the Path type
    :param path: The object to be converted to the Path Type
    :return: The input as Path object.
    """
    def _normalize(p: PathThing):
        result = str(p)
        if not isinstance(p, Path) and not isinstance(p, os.PathLike) and not isinstance(p, str):
            raise TypeError('Invalid type for path: p'.format(result))
        return result
    return [_normalize(p) for p in paths]


def _check_paths(paths: List[str]):
    """
    Checks whether the Paths exists and points to a
    :param paths:
    :return:
    """
    illegal_paths = [path for path in paths if not _file_is_valid(path)]
    if illegal_paths:
        paths = ','.join([str(path) for path in paths])
        raise IllegalResponseException(
             "RunAlgorithmResponse found to be invalid,"
             " since the following paths are not allowed to be exported: {}".format(paths))


class RebaseStrategy(Typed):
    def __init__(self,
                 next_train_tag: str,
                 export_files: List[PathThing]):
        # Next train tag
        self.next_train_tag: str = next_train_tag

        if not _train_tag_is_valid(self.next_train_tag):
            raise IllegalResponseException('Next train tag {} is invalid!'.format(self.next_train_tag))

        # The exported files
        self.export_files = _normalize_paths(export_files)
        _check_paths(self.export_files)

    @property
    def data(self) -> dict:
        return {
            'export_files': self.export_files,
            'next_train_tag': self.next_train_tag
        }
