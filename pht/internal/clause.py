from typing import Set


class Clause:
    """
    A clause is a set of literals. Here we represent literals simply as signed integers
    """
    def __init__(self, first_literal: int, *more_literals: int):

        tmp_set: Set[int] = {x for x in more_literals}
        tmp_set.add(first_literal)
        self._literals = frozenset(tmp_set)

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

    def __hash__(self):
        return hash(self._literals)

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()

    def copy(self):
        return Clause(*self._literals)
