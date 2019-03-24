from collections.abc import Hashable
from .Formula import Formula
from .Clause import Clause, frozen_set_of


class CNF(Hashable, Formula):
    def __init__(self, clause: Clause, *clauses: Clause):
        self._clauses = frozen_set_of(Clause, clause, clauses)

    @property
    def type_name(self) -> str:
        return 'ConjunctiveNormalForm'

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        return iter(self._clauses)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._clauses)

    def __contains__(self, item):
        return item in self._clauses

    def __hash__(self):
        return hash(self._clauses)

    def deepcopy(self):
        return CNF(*self._clauses)

    @property
    def value(self):
        return sorted([sorted([i for i in clause]) for clause in self])
