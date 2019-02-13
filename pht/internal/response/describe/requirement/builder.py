import abc
from typing import Dict, List
from pht.internal.response.describe.formula import Clause
from pht.internal.util.builder import \
    ConjunctionBuilder,\
    DisjunctionBuilder,\
    DisjunctionComposite
from pht.internal.response.describe.property.Property import Property


class _Literal(ConjunctionBuilder, DisjunctionBuilder):

    def __init__(self, prop: Property):
        if not isinstance(prop, Property):
            raise ValueError('Argument \'{}\' of Literal is not a property'.format(str(prop)))
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
