"""
Contains the ListRequirementsResponse class, which belongs to the list_requirements command.

@author Lukas Zimmermann
"""
# from .Response import Response
# from pht.formula import Clause
# from pht.property import Property
# from typing import Union, List
#
#
# class ListRequirementsResponse(Response):
#     def __init__(self, clause: Union[Clause, ClauseContainer], unmet: List[Property] = None):
#         if isinstance(clause, Clause):
#             container = ClauseContainer([clause])
#         elif isinstance(clause, ClauseContainer):
#             container = clause
#         else:
#             raise ValueError("Passed formula is neither a single formula nor a formula container")
#
#         # Collect all requirements from the relations and give indices
#         requirements = [req for rel in container for req in rel]
#         req_dict = {req: i for (i, req) in enumerate(requirements)}
#
#         self.requirements = [{'id': i, 'property': req.to_dict()} for (i, req) in enumerate(requirements)]
#         self.relations = [{
#             'id': i,
#             'type': rel.type,
#             'requirements': [req_dict[req] for req in rel]
#         } for (i, rel) in enumerate(container.relations)]
#
#         self.unmet = None
#         if unmet is not None:
#             self.unmet = [req_dict[req] for req in unmet]
#
#     @property
#     def type(self):
#         return 'ListRequirementsResponse'
#
#     def to_dict(self):
#         result = {
#             'type': self.type,
#             'requirements': self.requirements,
#             'clauses': self.relations,
#             'check': False
#         }
#         # If also listing of unmet requirements is requested (self.unmet != None), these will also be included in the
#         # response
#         if self.unmet is not None:
#             result['check'] = True
#             result['unmet'] = self.unmet
#         return result
