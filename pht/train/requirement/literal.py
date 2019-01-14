import abc
from typing import Dict, List
from pht.property import Property
from pht.formula import Clause
from .builder import _ConjunctionBuilder, _DisjunctionBuilder, _DisjunctionBuilderImpl


class _Literal(_ConjunctionBuilder, _DisjunctionBuilder):

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


class Require(_Literal):
    @property
    def sign(self):
        return 1


class Forbid(_Literal):
    @property
    def sign(self):
        return -1


class Any(_ConjunctionBuilder):
    def __init__(self, dis: _DisjunctionBuilderImpl):
        if not isinstance(dis, _DisjunctionBuilderImpl):
            raise ValueError("Not a valid expression. Use '|' within Any")
        self._dis = dis

    @property
    def clauses(self) -> List[Clause]:
        return [self._dis.clause]

    @property
    def props(self) -> Dict[int, Property]:
        return self._dis.props
