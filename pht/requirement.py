"""
Primitives of the DSL for creating requirements for a train
"""
import abc
from typing import Dict, List
from pht.internal import \
    ConjunctionBuilder,\
    Clause,\
    DisjunctionBuilder,\
    DisjunctionComposite,\
    Property,\
    UrlEnvironmentVariableProperty


class _Literal(ConjunctionBuilder, DisjunctionBuilder):

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


class Any(ConjunctionBuilder):
    def __init__(self, dis: DisjunctionComposite):
        if not isinstance(dis, DisjunctionComposite):
            raise ValueError("Not a valid expression. Use '|' within Any")
        self._dis = dis

    @property
    def clauses(self) -> List[Clause]:
        return [self._dis.clause]

    @property
    def props(self) -> Dict[int, Property]:
        return self._dis.props


def url_by_name(name: str):
    return UrlEnvironmentVariableProperty(name)
