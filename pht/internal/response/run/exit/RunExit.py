"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
import abc
from collections.abc import Hashable
from typing import Optional
from pht.internal.protocol.Copyable import Copyable
from pht.internal.protocol.SimpleDictRepresentable import SimpleDictRepresentable


class RunExit(Copyable, Hashable, SimpleDictRepresentable):
    def __init__(self, reason: Optional[str]):
        self.reason = reason

    @property
    @abc.abstractmethod
    def state(self) -> str:
        pass

    def __hash__(self):
        return hash((self.reason, self.state))

    def _as_dict(self):
        return {
            'state': self.state,
            'reason': self.reason
        }


class AlgorithmSuccess(RunExit):

    @property
    def state(self) -> str:
        return 'success'

    def copy(self):
        return AlgorithmSuccess(self.reason)


class AlgorithmFailure(RunExit):

    @property
    def state(self) -> str:
        return 'failure'

    def copy(self):
        return AlgorithmFailure(self.reason)


class AlgorithmApplication(RunExit):

    @property
    def state(self) -> str:
        return 'application'

    def copy(self):
        return AlgorithmApplication(self.reason)
