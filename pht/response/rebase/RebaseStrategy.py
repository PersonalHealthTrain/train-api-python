from abc import ABC, abstractmethod


class RebaseStrategy(ABC):

    @property
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass


class DockerRebaseStrategy(RebaseStrategy):

    def __init__(self, frm: str):
        self.frm = frm

    @property
    def type(self):
        return 'docker'

    def to_dict(self):
        return {
            'type': self.type,
            'from': self.frm
        }
