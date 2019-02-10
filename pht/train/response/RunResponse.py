"""
Contains the RunResponse class
"""
import json
from pht.rebase import RebaseStrategy
from pht.train.response.exit_state import AlgorithmExitState


class RunResponse:
    """
    Response for the run command
    """
    def __init__(self,
                 state: AlgorithmExitState,
                 state_reason: str,
                 free_text_message: str,
                 rebase: RebaseStrategy):

        # Final Execution State of the algorithm
        self.exit_state = state

        # Reason for setting the Algorithm exit state to the respective value. E.g. in case of failure, this
        # might be an error message
        self.exit_state_reason = state_reason

        # Custom message to communicate the execution state of the algorithm
        self.message = free_text_message

        # The Rebase Strategy
        self.rebase = rebase

    @property
    def type(self) -> str:
        return 'RunResponse'

    def dict(self) -> dict:
        return {
            'exit_state': self.exit_state.value,
            'exit_state_reason': self.exit_state_reason,
            'free_text_message': self.message,
            'rebase': self.rebase.dict()
        }

    def to_json_string(self):
        return json.dumps(self.dict())
