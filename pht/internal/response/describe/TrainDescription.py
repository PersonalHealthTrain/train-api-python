from typing import Dict, List, Optional
from pht.internal.response.TrainResponse import TrainResponse
from pht.internal.response.describe.property.Property import Property
from pht.internal.response.describe.formula.Formula import Formula
from pht.internal.response.describe.algorithm.AlgorithmRequirement import AlgorithmRequirement


class TrainDescription(TrainResponse):
    """
    Description of a train that is obtained when the train is invoked with the describe command
    """
    def __init__(self,
                 properties: Dict[int, Property],
                 formulas: List[Formula],
                 model_summary: str,
                 train_name: str,
                 algorithm_requirement: Optional[AlgorithmRequirement]):
        self._properties = properties
        self._formula = formulas
        self._model_summary = model_summary
        self._algorithm_requirement = algorithm_requirement
        self._train_name = train_name

    @property
    def data(self) -> dict:

        def with_ids(iterable, id_fun, data_fun):
            return [{'id': id_fun(x), 'data': data_fun(x)} for x in iterable]
        first_with_dict = lambda x: x[1].as_dict()
        properties = with_ids(self._properties.items(), id_fun=lambda x: x[0], data_fun=first_with_dict)
        formula = with_ids(enumerate(self._formula), id_fun=lambda x: x[0]+1, data_fun=first_with_dict)
        return {
            'trainName': self._train_name,
            'version': '1.0',
            'properties': properties,
            'formula': formula,
            'model': {
                'summary': self._model_summary
            },
            'algorithm': {
                'requirement': self._algorithm_requirement.as_dict() if self._algorithm_requirement is not None else None
            }
        }

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'TrainDescription'
