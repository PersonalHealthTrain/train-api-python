import json
import os
import re
from functools import total_ordering
from typing import Union
from .TrainFile import TrainFile
from pht.internal.util import require


_KEY_REGEX = re.compile(r'[a-zA-Z_][a-zA-Z0-9_-]*')


def _is_valid_key(key: str):
    return _KEY_REGEX.fullmatch(key) is not None


@total_ordering
class ModelFile(TrainFile):
    def __init__(self, key: str):
        require.for_value(key, lambda x: _is_valid_key(x), 'String: {} is not a valid key for TrainFile'.format(key))
        self._key = key
        self._path = os.path.join(ModelFile.base_dir(), key)

    def copy(self):
        return ModelFile(self._key)

    @property
    def absolute_path(self) -> str:
        return self._path

    @property
    def type(self) -> str:
        return self.type_name

    @property
    def type_name(self) -> str:
        return 'ModelFile'

    @staticmethod
    def base_dir():
        return os.path.join(TrainFile.base_dir(), 'model')

    def write(self, content: Union[str, list, dict]):
        with open(self._path, 'w') as f:
            if isinstance(content, str):
                f.write(content)
            else:
                json.dump(content, f)

    def read(self):
        with open(self._path, 'r') as f:
            content = os.linesep.join(f.readlines())
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return content

    def read_or_default(self, default: str):
        if os.path.isfile(self._path):
            return self.read()
        return default
