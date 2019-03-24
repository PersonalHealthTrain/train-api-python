"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
import abc
from collections.abc import Hashable
from typing import Optional
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass


class RunExit(Hashable, TypedAsPythonClass):
    def __init__(self, reason: Optional[str]):
        self.reason = reason

    @property
    @abc.abstractmethod
    def state(self) -> str:
        pass

    def __hash__(self):
        return hash((self.reason, self.state))

    @property
    def data(self) -> dict:
        return {
            'state': self.state,
            'reason': self.reason
        }


class AlgorithmSuccessRunExit(RunExit):

    @property
    def state(self) -> str:
        return 'success'

    def deepcopy(self):
        return AlgorithmSuccessRunExit(self.reason)


class AlgorithmFailureRunExit(RunExit):

    @property
    def state(self) -> str:
        return 'failure'

    def deepcopy(self):
        return AlgorithmFailureRunExit(self.reason)


class AlgorithmApplicationRunExit(RunExit):

    @property
    def state(self) -> str:
        return 'application'

    def deepcopy(self):
        return AlgorithmApplicationRunExit(self.reason)
