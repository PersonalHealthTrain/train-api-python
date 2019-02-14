import json
import os
import re
from typing import AnyStr
from pht.internal.protocol.Comparable import Comparable
from pht.internal.protocol.Typed import Typed
from pht.internal.util import require

_KEY_REGEX = re.compile(r'[a-zA-Z_][a-zA-Z0-9_-]*')


def _is_valid_key(key: str):
    return _KEY_REGEX.fullmatch(key) is not None


class TrainFile(Comparable, Typed):
    def __init__(self, key: str):
        require.for_value(key, lambda x: _is_valid_key(x), 'String: {} is not a valid key for TrainFile'.format(key))
        self._path = os.path.join('/opt', 'train', key)

    def __eq__(self, other):
        return other is self or \
               (isinstance(other, TrainFile) and self._path == other._path)

    def __hash__(self):
        return hash(self._path)

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'TrainFile'

    @property
    def data(self) -> dict:
        return {
            'path': self._path
        }

    @property
    def path(self):
        return self._path

    def write(self, content: AnyStr):
        with open(self._path, 'w') as f:
            f.write(content)

    def write_as_json(self, obj):
        self.write(json.dumps(obj))

    def read(self):
        with open(self._path, 'r') as f:
            return os.linesep.join(f.readlines())
