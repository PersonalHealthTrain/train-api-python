from typing import Set


class Clause:
    """
    A clause is a set of literals. Here we represent literals simply as signed integers
    """
    def __init__(self, first_literal: int, *more_literals: int):

        self._literals: Set[int] = {x for x in more_literals}
        self._literals.add(first_literal)

        # 0 is not allowed as a literal
        if 0 in self._literals:
            raise ValueError("0 is not allowed as a literal for a clause")

    def __iter__(self):
        return iter(self._literals)

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Clause):
            return False
        return self._literals == other._literals

    def copy(self):
        return Clause(*self._literals)
