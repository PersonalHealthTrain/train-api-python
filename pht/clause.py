from abc import abstractmethod
from typing import List
from pht.property.Property import Property



class AllClause(Clause):
    def __init__(self, requirements: List[Property]):
        self._requirements = requirements.copy()

    @property
    def requirements(self) -> List[Property]:
        return self._requirements

    @property
    def type(self):
        return 'all'


class AnyClause(Clause):
    def __init__(self, requirements: List[Property]):
        self._requirements = requirements.copy()

    @property
    def requirements(self) -> List[Property]:
        return self._requirements

    @property
    def type(self):
        return 'any'


def require_all(*requirements):
    return AllClause(list(requirements))


def require_any(*requirements):
    return AnyClause(list(requirements))


class ClauseContainer:
    """
    Wraps a list of relations for requirements.
    """
    def __init__(self, relations: List[Clause]):
        self.relations = relations.copy()

    def __iter__(self):
        return iter(self.relations)

    def __add__(self, other):
        if isinstance(other, Clause):
            return ClauseContainer(self.relations + [other])
