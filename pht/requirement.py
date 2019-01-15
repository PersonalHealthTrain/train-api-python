from typing import Dict, List
from pht.internal import Clause, Literal, ConjunctionBuilder, DisjunctionComposite

class Require(Literal):
    @property
    def sign(self):
        return 1


class Forbid(Literal):
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
