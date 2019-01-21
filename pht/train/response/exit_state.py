"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
import enum


class AlgorithmExitState(enum.Enum):
    """
    Encodes the exit state of the train-encapsulated algorithm.
    """
    # Algorithm has terminated successfully
    SUCCESS = 'success'

    # Algorithm has failed
    FAILURE = 'failure'

    # Application-specific exit status of the algorithm (reserved for later usage)
    APPLICATION = 'application'


SUCCESS = AlgorithmExitState.SUCCESS
FAILURE = AlgorithmExitState.FAILURE
APPLICATION = AlgorithmExitState.APPLICATION
