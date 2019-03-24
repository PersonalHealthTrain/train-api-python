from collections.abc import Hashable, Sized
from pht.internal.util import require
from pht.internal.util import frozen_set_of
from pht.internal.protocol.DeepCopyable import DeepCopyable


class Clause(DeepCopyable, Hashable, Sized):
    """
    A clause is a set of literals. Here we represent literals simply as signed integers
    """
    def __init__(self, first_literal: int, *more_literals: int):
        self._literals = frozen_set_of(int, first_literal, more_literals)
        for literal in self._literals:
            require.type_is_int(literal)
        require.for_value(self._literals,
                          that=lambda x: 0 not in x,
                          error_if_not="0 is not allowed as a literal for a clause")

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
        return other is self or \
               (isinstance(other, Clause) and self._literals == other._literals)

    def __hash__(self):
        return hash(self._literals)

    def deepcopy(self):
        return Clause(*self._literals)
