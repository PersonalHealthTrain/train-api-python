import abc
from typing import Dict, List
from pht.internal.describe.formula import Clause
from pht.internal.describe.property.Property import Property


def _copy(d: Dict[int, Property]):
    return {
        i: prop.copy() for (i, prop) in d.items()
    }


def _merge(left: Dict[int, Property], right: Dict[int, Property], clauses: List[Clause]):
    """
     Merges this Property with the other property map without changing this one.
    """
    remap = {}
    new_properties = _copy(left)

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
