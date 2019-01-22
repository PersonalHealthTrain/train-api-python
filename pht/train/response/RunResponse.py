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
                 free_text_message: str,
                 rebase: RebaseStrategy):

        # Final Execution State of the algorithm
        self.state = state

        # Custom message to communicate the execution state of the algorithm
        self.message = free_text_message

        # The Rebase Strategy
        self.rebase = rebase

    @property
    def type(self) -> str:
        return 'RunResponse'

    def dict(self) -> dict:
        return {
            'state': self.state.value,
            'free_text_message': self.message,
            'rebase': self.rebase.dict()
        }

    def to_json_string(self):
        return json.dumps(self.dict())
