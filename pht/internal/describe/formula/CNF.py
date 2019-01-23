from .Formula import Formula
from pht.internal import Clause, frozen_set_of


class CNF(Formula):
    def __init__(self, clause: Clause, *clauses: Clause):
        self._clauses = frozen_set_of(Clause, clause, clauses)

    @property
    def type(self) -> str:
        return 'https://www.wikidata.org/wiki/Q846564'

    @property
    def display(self) -> str:
        return 'ConjunctiveNormalForm'

    def __str__(self):
        return str(self.value())

    def __iter__(self):
        return iter(self._clauses)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._clauses)

    def __contains__(self, item):
        return item in self._clauses

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, CNF):
            return False
        return self._clauses == other._clauses

    def __hash__(self):
        return hash(self._clauses)

    def copy(self):
        return CNF(*self._clauses)

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()

    def value(self):
        return sorted([sorted([i for i in clause]) for clause in self])
