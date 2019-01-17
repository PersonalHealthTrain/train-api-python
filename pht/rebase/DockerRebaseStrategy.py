

from .RebaseStrategy import RebaseStrategy


class DockerRebaseStrategy(RebaseStrategy):

    def __init__(self, frm: str):
        self.frm = frm

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'docker'

    @property
    def data(self) -> dict:
        return {
            'from': self.frm
        }
