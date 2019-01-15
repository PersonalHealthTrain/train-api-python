import abc
from typing import Dict, List
from pht.internal import Clause, ConjunctionBuilder, DisjunctionBuilder, Property


class Literal(ConjunctionBuilder, DisjunctionBuilder):

    def __init__(self, prop: Property):
        self._prop = prop.copy()
        self._literal = 1
        self._clause = Clause(self.sign * self._literal)

    @property
    def clauses(self) -> List[Clause]:
        return [self._clause]

    @property
    def clause(self) -> Clause:
        return self._clause

    @property
    def props(self) -> Dict[int, Property]:
        return {self._literal: self._prop}

    @property
    @abc.abstractmethod
    def sign(self):
        pass
