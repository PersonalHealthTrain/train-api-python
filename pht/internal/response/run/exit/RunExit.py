"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
from abc import abstractmethod
from collections.abc import Hashable
from typing import Optional
from pht.internal.typesystem.TypedAsPythonClass import TypedAsPythonClass
from pht.internal.util import require


class RunExit(Hashable, TypedAsPythonClass):
    """Base class for declaring the RunExit"""
    def __init__(self, reason: Optional[str]):
        self._reason = reason
        require.type_is_str_or_none(self._reason)

    @property
    def reason(self):
        """Textual representation of the reason why the exit State has been set this way"""
        return self._reason

    @property
    @abstractmethod
    def state(self) -> str:
        """Textual representation of the Exit State"""
        pass

    def __hash__(self):
        return hash((self.reason, self.state))

    @property
    def data(self) -> dict:
        """Data of RunExit"""
        return {
            'state': self.state,
            'reason': self.reason
        }


class AlgorithmSuccessRunExit(RunExit):
    """Algorithm was exited successfully"""

    @property
    def state(self) -> str:
        """State of the Algorithm Execution"""
        return 'success'

    def deepcopy(self):
        """Returns Deep Copy of this RunExit"""
        return AlgorithmSuccessRunExit(self.reason)


class AlgorithmFailureRunExit(RunExit):
    """Algorithm has failed"""

    @property
    def state(self) -> str:
        """State of the Algorithm Execution"""
        return 'failure'

    def deepcopy(self):
        """Returns Deep Copy of this RunExit"""
        return AlgorithmFailureRunExit(self.reason)


class AlgorithmApplicationRunExit(RunExit):
    """Run Exit of Algorithm is Application specific"""
    @property
    def state(self) -> str:
        """State of the Algorithm Execution"""
        return 'application'

    def deepcopy(self):
        """Returns Deep Copy of this RunExit"""
        return AlgorithmApplicationRunExit(self.reason)
