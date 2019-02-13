from typing import List
from .RebaseStrategy import RebaseStrategy, PathThing


class DockerRebaseStrategy(RebaseStrategy):

    def __init__(self,
                 frm: str,
                 next_train_tags: List[str],
                 export_files: List[PathThing]):
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
        return hash((self.frm, self.next_train_tags, ''.join(sorted(self.export_files))))

    def copy(self):
        return DockerRebaseStrategy(self.frm, list(self.next_train_tags), self.export_files)
