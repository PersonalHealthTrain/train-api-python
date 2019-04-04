"""
Contains the ModelFile class
"""
import json
import os
import re
from functools import total_ordering
from typing import Union
from .TrainFile import TrainFile
from pht.internal.util import require


def _make_key_validator():
    _KEY_REGEX = re.compile(r'[a-zA-Z_][a-zA-Z0-9_-]*')
    return lambda potential_key: _KEY_REGEX.fullmatch(potential_key) is not None


_is_valid_key = _make_key_validator()


@total_ordering
class ModelFile(TrainFile):
    """"A Model File is a file in the file system that belongs to the model of the train"""
    def __init__(self, key: str):
        self._key = key
        require.type_is_str(self._key)
        require.for_value(self._key,
                          that=lambda x: _is_valid_key(x),
                          error_if_not='String: {} is not a valid key for TrainFile'.format(self._key))
        self._path = os.path.join(ModelFile.base_dir(), key)

    def deepcopy(self):
        """Returns deepcopy of ModelFile object"""
        return ModelFile(self._key)

    @property
    def absolute_physical_path(self) -> str:
        """The absolute physical path of the Model File"""
        return self._path

    @staticmethod
    def base_dir():
        """Where Model Files are located on the File System"""
        return os.path.join(TrainFile.base_dir(), 'model')

    def write(self, content: Union[str, list, dict]):
        """Writes the content as JSON if its a list or dict, else it is written as str"""
        with open(self._path, 'w') as f:
            if isinstance(content, str):
                f.write(content)
            else:
                json.dump(content, fp=f)

    def read(self):
        """Loads JSON if the content of the file if JSON, otherwise just loads the string representation"""
        with open(self._path, 'r') as f:
            content = os.linesep.join(f.readlines())
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return content

    def read_or_default(self, default: str):
        """Reads the content of the file if present, otherwise returns the default value"""
        if os.path.isfile(self._path):
            return self.read()
        return default
