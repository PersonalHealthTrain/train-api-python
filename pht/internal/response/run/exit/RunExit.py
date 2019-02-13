"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
import abc
from typing import Optional
from pht.internal.protocols import Comparable, Copyable, DictRepresentable


class RunExit(Comparable, Copyable, DictRepresentable):
    def __init__(self, reason: Optional[str]):
        self.reason = reason

    @property
    @abc.abstractmethod
    def state(self) -> str:
        pass

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, RunExit):
            return False
        return self.reason == other.reason and self.state == other.state

    def __hash__(self):
        return hash((self.reason, self.state))

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()

    def dict(self):
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
