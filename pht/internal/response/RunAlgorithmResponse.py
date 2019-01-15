"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
import os
from typing import List, Union
from enum import Enum
from pathlib import Path
from .IllegalResponse import IllegalResponse
from .Response import Response
from pht.internal.rebase import RebaseStrategy


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


class AlgorithmExitState(Enum):
    """
    Encodes the exit state of the train-encapsulated algorithm.
    """
    # Algorithm has terminated successfully
    SUCCESS = 'success'

    # Algorithm has failed
    FAILURE = 'failure'

    # Application-specific exit status of the algorithm (reserved for later usage)
    APPLICATION = 'application'


class RunAlgorithmResponse(Response):
    """
    Response for the run_algorithm command
    """
    def __init__(self,
                 state: AlgorithmExitState,
                 message: str,
                 next_train_tag: str,
                 rebase: RebaseStrategy,
                 export_files: List[Union[Path, str, os.PathLike]]):

        # Final Execution State of the algorithm
        self.state = state

        # Custom message to communicate the execution state of the algorithm
        self.message = message

        # The next train tag that the new train image should be created with
        self.next_train_tag = next_train_tag

        # The Rebase Strategy
        self.rebase = rebase

        # List of files (with absolute paths) that should be exported from the exited container
        self.export_files = [_normalize_path(path) for path in export_files]
        RunAlgorithmResponse._check_paths(self.export_files)

    @staticmethod
    def _check_paths(paths: List[Path]):
        """
        Checks whether the Paths exists and points to a
        :param paths:
        :return:
        """
        illegal_paths = [path for path in paths if not RunAlgorithmResponse._file_is_valid(path)]
        if illegal_paths:
            paths = ','.join([str(path) for path in paths])
            raise IllegalResponse(
                "RunAlgorithmResponse found to be invalid,"
                " since the following paths are not allowed to be exported: {}".format(paths))

    @staticmethod
    def _file_is_valid(path: Path) -> bool:
        """
        Checks that the file referenced by the path is an existing regular file and not a symlink. Also, the
        path needs to be absolute.
        :param path: The path to be tested
        :return: Whether the path is valid as defined above
        """
        return path.is_absolute() and path.is_file() and not path.is_symlink()

    @property
    def type(self) -> str:
        return 'RunAlgorithmResponse'

    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'state': self.state.name,
            'message': self.message,
            'next_train_tag': self.next_train_tag,
            'rebase': self.rebase.to_dict(),
            'export_files': self.export_files
        }
