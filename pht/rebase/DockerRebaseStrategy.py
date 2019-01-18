from typing import List
from .RebaseStrategy import RebaseStrategy, PathThing


class DockerRebaseStrategy(RebaseStrategy):

    def __init__(self,
                 frm: str,
                 next_train_tag: str,
                 export_files: List[PathThing]):
        super().__init__(next_train_tag, export_files)
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
