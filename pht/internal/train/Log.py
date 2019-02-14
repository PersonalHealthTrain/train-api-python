from typing import List
from pht.internal.response.run.exit.RunExit import AlgorithmSuccess, RunExit


class Log:
    def __init__(self):
        self.exit_state = AlgorithmSuccess('')
        self.free_text_message = ''
        self.rebase_from = None
        self.next_train_tags = None

    def set_exit_state(self, exit_state: RunExit):
        self.exit_state = exit_state

    def set_free_text_message(self, m: str):
        self.free_text_message = m

    def set_rebase_from(self, frm: str):
        self.rebase_from = frm

    def set_next_train_tags(self, tags: List[str]):
        self.next_train_tags = tags.copy()
