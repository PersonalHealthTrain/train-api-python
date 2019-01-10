from abc import abstractmethod
from typing import List
from pht.response.requirement.Requirement import Requirement


class Clause:
    """
    A Relation is a list of related requirements
    """

    @property
    @abstractmethod
    def requirements(self) -> List[Requirement]:
        pass

    @property
    @abstractmethod
    def type(self):
        pass

    def to_dict(self):
        return {
            self.type: [req.to_dict() for req in self.requirements]
        }

    def __iter__(self):
        return iter(self.requirements)

    def __add__(self, other):
        if isinstance(other, Clause):
            return ClauseContainer([self, other])
        if isinstance(other, ClauseContainer):
            return ClauseContainer(other.relations + [self])
        raise TypeError("Unsupported Operation + for type {}".format(other.__class__.__name__))


class AllClause(Clause):
    def __init__(self, requirements: List[Requirement]):
        self._requirements = requirements.copy()

    @property
    def requirements(self) -> List[Requirement]:
        return self._requirements

    @property
    def type(self):
        return 'all'


class AnyClause(Clause):
    def __init__(self, requirements: List[Requirement]):
        self._requirements = requirements.copy()

    @property
    def requirements(self) -> List[Requirement]:
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
