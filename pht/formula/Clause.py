from typing import Set


class Clause:
    """
    A clause is a set of literals. Here we represent literals simply as signed integers
    """

    def __init__(self, *literals: int):
        self.literals: Set[int] = {x for x in literals}

    def __iter__(self):
        return iter(self.literals)
