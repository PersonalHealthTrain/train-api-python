import abc
from typing import Dict, List
from copy import deepcopy

from pht.internal.response.describe.property.Property import Property
from pht.internal.response.describe.formula.Clause import Clause
from pht.internal.response.describe.formula.CNF import ConjunctiveNormalForm


def copy_property_map(d: Dict[int, Property]):
    return {
        i: prop.deepcopy() for (i, prop) in d.items()
    }


def _merge(left: Dict[int, Property], right: Dict[int, Property], clauses: List[Clause]):
    """
     Merges this Property with the other property map without changing this one.
    """
    remap = {}
    new_properties = copy_property_map(left)

    next_key = max(new_properties.keys())
    for (other_key, other_value) in right.items():
        if other_value in new_properties.values():
            for (self_key, self_value) in new_properties.items():
                if self_value == other_value:
                    remap[other_key] = self_key
                    break
        else:
            next_key += 1
            new_properties[next_key] = other_value
            remap[other_key] = next_key

    # construct the new other clauses
    def new_literal(i):
        a = abs(i)
        if a not in remap:
            return i
        v = remap[a]
        return -v if i < 0 else v

    other_clauses = [Clause(*{new_literal(i) for i in clause}) for clause in clauses]
    return new_properties, other_clauses


class _PropertyEnumerator(abc.ABC):
    @property
    @abc.abstractmethod
    def props(self) -> Dict[int, Property]:
        pass


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
        return ConjunctiveNormalForm(*self.clauses)


class ConjunctionComposite(ConjunctionBuilder):
    def __init__(self, clauses: List[Clause], props: Dict[int, Property]):
        self._clauses = deepcopy(clauses)
        self._props = copy_property_map(props)

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
        self._clause = clause.deepcopy()
        self._props = copy_property_map(props)

    @property
    def clause(self) -> Clause:
        return self._clause

    @property
    def props(self) -> Dict[int, Property]:
        return self._props
