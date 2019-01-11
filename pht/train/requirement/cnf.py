from typing import Set, Dict, List
from pht.formula import CNF
from pht.formula import Clause
from .AlgorithmRequirement import AlgorithmRequirement
from pht.property import Property


class CnfAlgorithmRequirement(AlgorithmRequirement):
    def __init__(self, cnf: CNF):
        self.cnf = cnf


class CnfBuilder:

    def __init__(self, clauses: List[Clause], props: Dict[int, Property]):
        self.clauses: List[Clause] = clauses.copy()
        self.props = props.copy()

    def __and__(self, other):
        if not isinstance(other, CnfBuilder):
            raise ValueError('Cannot \'and\' CnfBuilder and class {}. Must and to CnfBuilder.'.format(other.__class__))

        # remaps
        remap = {}
        new_properties = self.props.copy()

        next_key = max(new_properties.keys())
        for (other_key, other_value) in other.props.items():
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

        other_clauses = [Clause(*{new_literal(i) for i in clause.literals}) for clause in other.clauses]
        return CnfBuilder(self.clauses + other_clauses, new_properties)

    def cnf(self):
        return CNF(*self.clauses)


class Require(CnfBuilder):
    def __init__(self, prop: Property):
        super().__init__([Clause(1)], {1: prop})


class Forbid(CnfBuilder):
    def __init__(self, prop: Property):
        super().__init__([Clause(-1)], {1: prop})
