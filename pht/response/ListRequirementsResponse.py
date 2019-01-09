from .Response import Response
from .requirement.clause import Clause, ClauseContainer
from typing import Union


class ListRequirementsResponse(Response):
    def __init__(self, relation: Union[Clause, ClauseContainer]):
        if isinstance(relation, Clause):
            container = ClauseContainer([relation])
        elif isinstance(relation, ClauseContainer):
            container = relation
        else:
            raise ValueError("Passed clause is neither a single clause nor a clause container")

        # Collect all requirements from the relations and give indices
        requirements = [req for rel in container for req in rel]
        self.req_dict = {req: i for (i, req) in enumerate(requirements)}

        self.requirements = [{'id': i, 'requirement': req.to_dict()} for (i, req) in enumerate(requirements)]
        self.relations = [{
            'id': i,
            'type': rel.type,
            'requirements': [self.req_dict[req] for req in rel]
        } for (i, rel) in enumerate(container.relations)]

    def to_dict(self):
        return {
            'requirements': self.requirements,
            'clauses': self.relations
        }
