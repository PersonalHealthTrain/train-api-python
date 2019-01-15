from typing import List
from .Formula import Formula
from pht.internal import Clause


class CNF(Formula):
    def __init__(self, *clauses: Clause):
        self.clauses: List[Clause] = [clause.copy() for clause in clauses]

    @property
    def type(self) -> str:
        return 'https://www.wikidata.org/wiki/Q846564'

    @property
    def display(self) -> str:
        return 'ConjunctiveNormalForm'

    def __str__(self):
        return str(sorted([sorted([i for i in clause]) for clause in self.clauses]))

    def value(self) -> dict:
        return {
            'array': [[i for i in clause] for clause in self.clauses]
        }
