import abc
from typing import Dict, List

from pht.internal.response.describe.property.Property import Property
from pht.internal.response.describe.formula.Clause import Clause
from pht.internal.response.describe.formula.CNF import CNF
from pht.internal.util.property_enumerator import _PropertyEnumerator, _copy, _merge


class ConjunctionBuilder(_PropertyEnumerator):

    @property
    @abc.abstractmethod
    def clauses(self) -> List[Clause]:
        pass

    def __and__(self, other):
        if not isinstance(other, ConjunctionBuilder):
            raise ValueError(
                'Cannot \'and\' CnfBuilder and class {}. Must and to CnfBuilder.'.format(other.__class__))

        new_properties, other_clauses = _merge(self.props, other.props, other.clauses)
        return ConjunctionComposite(self.clauses + other_clauses, new_properties)

    def cnf(self):
        return CNF(*self.clauses)


class ConjunctionComposite(ConjunctionBuilder):
    def __init__(self, clauses: List[Clause], props: Dict[int, Property]):
        self._clauses = [clause.copy() for clause in clauses]
        self._props = _copy(props)

    @property
    def clauses(self) -> List[Clause]:
        return self._clauses

    @property
    def props(self) -> Dict[int, Property]:
        return self._props


class DisjunctionBuilder(_PropertyEnumerator):

    def __or__(self, other):
        if not isinstance(other, DisjunctionBuilder):
            raise ValueError(
                'Cannot \'or\' CnfBuilder and class {}. Must and to CnfBuilder.'.format(other.__class__))

        new_properties, other_clauses = _merge(self.props, other.props, [other.clause])
        new_clause = Clause(*{i for i in self.clause}.union(other_clauses[0]))
        return DisjunctionComposite(new_clause, new_properties)

    @property
    @abc.abstractmethod
    def clause(self) -> Clause:
        pass


class DisjunctionComposite(DisjunctionBuilder):
    def __init__(self, clause: Clause, props: Dict[int, Property]):
        self._clause = clause.copy()
        self._props = _copy(props)

    @property
    def clause(self) -> Clause:
        return self._clause

    @property
    def props(self) -> Dict[int, Property]:
        return self._props
