"""
Contains the RunResponse class
"""
from pht.internal.response.run.rebase.RebaseStrategy import RebaseStrategy
from pht.internal.response.run.exit.RunExit import RunExit
from pht.internal.response.TrainResponse import TrainResponse


class RunResponse(TrainResponse):
    """
    Response for the run command
    """
    def __init__(self,
                 run_exit: RunExit,
                 free_text_message: str,
                 rebase: RebaseStrategy):

        # Final Execution State of the algorithm
        self.run_exit = run_exit.copy()

        # Custom message to communicate the execution state of the algorithm
        self.message = free_text_message

        # The Rebase Strategy
        self.rebase = rebase.copy()

    def copy(self):
        return RunResponse(self.run_exit, self.message, self.rebase)

    def __hash__(self) -> int:
        return hash((self.run_exit, self.message, self.rebase))

    @property
    def data(self) -> dict:
        return {
            'runResponseVersion': '1.0',
            'exit': self.run_exit.as_simple_dict(),
            'freeTextMessage': self.message,
            'rebase': self.rebase.as_simple_dict()
        }
