from typing import Any, Iterable


def frozen_set(item, items: Iterable[Any]):
    tmp = {i for i in items}
    tmp.add(item)
    return frozenset(tmp)


class Clause:
    """
    A clause is a set of literals. Here we represent literals simply as signed integers
    """
    def __init__(self, first_literal: int, *more_literals: int):

        self._literals = frozen_set(first_literal, more_literals)

        # 0 is not allowed as a literal
        if 0 in self._literals:
            raise ValueError("0 is not allowed as a literal for a clause")

    def __iter__(self):
        return iter(self._literals)

    def __str__(self):
        return str(sorted(list(self)))

    def __repr__(self):
        return self.__str__()

    def __contains__(self, item):
        return item in self._literals

    def __len__(self):
        return len(self._literals)

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
