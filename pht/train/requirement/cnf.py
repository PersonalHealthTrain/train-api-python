import abc
from typing import Dict, List
from pht.formula import CNF
from pht.formula import Clause
from pht.property import Property


# class CnfAlgorithmRequirement(AlgorithmRequirement):
#     def __init__(self, cnf: CNF):
#         self.cnf = cnf


# class _AnyArgument:
#     def __init__(self, clause: Clause,  props: Dict[int, Property]):
#         self._clause = clause.copy()
#         self._props = props.copy()
#


class _ConjunctionBuilder(abc.ABC):

    @property
    @abc.abstractmethod
    def clauses(self) -> List[Clause]:
        pass

    @property
    @abc.abstractmethod
    def props(self) -> Dict[int, Property]:
        pass

    def __and__(self, other):
        if not isinstance(other, _ConjunctionBuilder):
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

        other_clauses = [Clause(*{new_literal(i) for i in clause}) for clause in other.clauses]
        return _ConjunctionBuilderImpl(self.clauses + other_clauses, new_properties)

    def cnf(self):
        return CNF(*self.clauses)


class _ConjunctionBuilderImpl(_ConjunctionBuilder):
    def __init__(self, clauses: List[Clause], props: Dict[int, Property]):
        self._clauses: List[Clause] = clauses.copy()
        self._props = props.copy()

    @property
    def clauses(self) -> List[Clause]:
        return self.clauses

    @property
    def props(self) -> Dict[int, Property]:
        return self.props


class _Literal(_ConjunctionBuilder):

    def __init__(self, prop: Property):
        self.prop = prop


    @property
    def clauses(self) -> List[Clause]:
        pass

    @property
    def props(self) -> Dict[int, Property]:
        pass

    @property
    @abc.abstractmethod
    def sign(self):
        pass



class Require(_ConjunctionBuilder):
    def __init__(self, prop: Property):
        self._clauses = [Clause(1)]
        self._props = {1: prop}

        #super().__init__(, )

    @property
    def clauses(self) -> List[Clause]:
        return self._clauses

    @property
    def props(self) -> Dict[int, Property]:
        return self._props


class Forbid(_ConjunctionBuilder):
    def __init__(self, prop: Property):
        super().__init__([Clause(-1)], {1: prop})

