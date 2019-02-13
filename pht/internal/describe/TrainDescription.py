import json
from typing import Dict, List, Optional
from pht.internal.describe.property import Property
from pht.internal.describe.formula import Formula
from pht.internal.describe.algorithm import AlgorithmRequirement


class TrainDescription:
    """
    Description of a train that is obtained when the train is invoked with the describe command
    """
    def __init__(self,
                 properties: Dict[int, Property],
                 formulas: List[Formula],
                 model_summary: str,
                 algorithm_requirement: Optional[AlgorithmRequirement]):
        self._properties = properties
        self._formula = formulas
        self._model_summary = model_summary
        self._algorithm_requirement = algorithm_requirement

    def to_json_string(self) -> str:
        return json.dumps(self.dict())

    def dict(self) -> dict:

        def with_ids(iterable, id_fun, data_fun):
            return [{'id': id_fun(x), 'data': data_fun(x)} for x in iterable]
        first_with_dict = lambda x: x[1].as_dict()
        properties = with_ids(self._properties.items(), id_fun=lambda x: x[0], data_fun=first_with_dict)
        formula = with_ids(enumerate(self._formula), id_fun=lambda x: x[0]+1, data_fun=first_with_dict)

        dictionary = {
            'properties': properties,
            'formula': formula,
            'model': {
                'summary': self._model_summary
            },
            'algorithm': {
                'requirement': self._algorithm_requirement.as_dict() if self._algorithm_requirement is not None else None
            }
        }
        return dictionary
