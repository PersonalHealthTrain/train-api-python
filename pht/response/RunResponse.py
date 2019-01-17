import json
import os
import re
from typing import List, Union
from pathlib import Path
from pht.internal import IllegalResponseException
from pht.rebase import RebaseStrategy
from .exit_state import AlgorithmExitState


_TRAIN_TAG_REGEX = re.compile(r'^[-.a-z0-9]+$')


def _train_tag_is_valid(value: str):
    return _TRAIN_TAG_REGEX.fullmatch(value) is not None


def _file_is_valid(path: Path) -> bool:
    """
    Checks that the file referenced by the path is an existing regular file and not a symlink. Also, the
    path needs to be absolute.
    :param path: The path to be tested
    :return: Whether the path is valid as defined above
    """
    return path.is_absolute() and path.is_file() and not path.is_symlink()


def _normalize_path(path: Union[Path, str, os.PathLike]) -> Path:
    """
    Converts several path Types to the Path type
    :param path: The object to be converted to the Path Type
    :return: The input as Path object.
    """
    if isinstance(path, str) or isinstance(path, os.PathLike):
        return Path(path)
    if isinstance(path, Path):
        return path
    raise ValueError('Error: Not a Path type: {}'.format(path.__class__))


def _check_paths(paths: List[Path]):
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


class RunResponse:
    """
    Response for the run_algorithm command
    """
    def __init__(self,
                 state: AlgorithmExitState,
                 free_text_message: str,
                 next_train_tag: str,
                 rebase: RebaseStrategy,
                 export_files: List[Union[Path, str, os.PathLike]]):

        # Final Execution State of the algorithm
        self.state = state

        # Custom message to communicate the execution state of the algorithm
        self.message = free_text_message

        # The next train tag that the new train image should be created with
        self.next_train_tag = next_train_tag

        if not _train_tag_is_valid(self.next_train_tag):
            raise IllegalResponseException('Next Train Tag {} is invalid!'.format(self.next_train_tag))

        # The Rebase Strategy
        self.rebase = rebase

        # List of files (with absolute paths) that should be exported from the exited container
        self.export_files = [_normalize_path(path) for path in export_files]
        _check_paths(self.export_files)

    @property
    def type(self) -> str:
        return 'RunAlgorithmResponse'

    def to_json_string(self) -> str:
        return json.dumps({
            'state': self.state.value,
            'message': self.message,
            'next_train_tag': self.next_train_tag,
            'rebase': self.rebase.dict(),
            'export_files': self.export_files
        })
