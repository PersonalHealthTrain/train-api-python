"""
Contains the RunResponse class
"""
import json
from pht.internal.run.rebase import RebaseStrategy
from pht.internal.run.exit.RunExit import RunExit


class RunResponse:
    """
    Response for the run command
    """
    def __init__(self,
                 run_exit: RunExit,
                 free_text_message: str,
                 rebase: RebaseStrategy):

        # Final Execution State of the algorithm
        self.run_exit = run_exit

        # Custom message to communicate the execution state of the algorithm
        self.message = free_text_message

        # The Rebase Strategy
        self.rebase = rebase

    @property
    def type(self) -> str:
        return 'RunResponse'

    def dict(self) -> dict:
        return {
            'exit': self.run_exit.dict(),
            'free_text_message': self.message,
            'rebase': self.rebase.dict()
        }

    def to_json_string(self):
        return json.dumps(self.dict())
