import json
import os
import re
from functools import total_ordering
from typing import AnyStr
from .TrainFile import TrainFile
from pht.internal.util import require


_KEY_REGEX = re.compile(r'[a-zA-Z_][a-zA-Z0-9_-]*')


def _is_valid_key(key: str):
    return _KEY_REGEX.fullmatch(key) is not None


@total_ordering
class ModelFile(TrainFile):
    def __init__(self, key: str):
        require.for_value(key, lambda x: _is_valid_key(x), 'String: {} is not a valid key for TrainFile'.format(key))
        self._path = os.path.join(ModelFile.base_dir(), key)

    @property
    def absolute_path(self) -> str:
        return self._path

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'ModelFile'

    def exists(self) -> bool:
        return os.path.isfile(self.absolute_path)

    @staticmethod
    def base_dir():
        return os.path.join(TrainFile.base_dir(), 'model')

    def write(self, content: AnyStr):
        with open(self._path, 'w') as f:
            f.write(content)

    def write_as_json(self, obj):
        self.write(json.dumps(obj))

    def read(self):
        with open(self._path, 'r') as f:
            return os.linesep.join(f.readlines())

    def read_or_default(self, default: str):
        if os.path.isfile(self._path):
            return self.read()
        return default
