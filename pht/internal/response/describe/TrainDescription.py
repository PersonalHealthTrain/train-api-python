from typing import Dict, List, Optional, Union
from pht.internal.response.TrainResponse import TrainResponse
from pht.internal.response.describe.property.Property import Property
from pht.internal.response.describe.formula.Formula import Formula
from pht.internal.response.describe.algorithm.AlgorithmRequirement import AlgorithmRequirement
from pht.internal.response.describe.model.ModelSummary import ModelSummary
from pht.internal.response.describe.model.StringModelSummary import StringModelSummary
from pht.internal.response.describe.model.JsonModelSummary import JsonModelSummary
from pht.internal.util.misc import as_dict_or_none


class TrainDescription(TrainResponse):
    """
    Description of a train that is obtained when the train is invoked with the describe command
    """
    def __init__(self,
                 train_name: str,
                 train_version: str,
                 properties: Dict[int, Property],
                 formulas: List[Formula],
                 model_summary: Union[ModelSummary, str, dict, list, None],
                 algorithm_requirement: Optional[AlgorithmRequirement]):
        self._properties = properties
        self._formula = formulas
        self._model_summary = model_summary
        if isinstance(self._model_summary, str):
            self._model_summary = StringModelSummary(self._model_summary)
        elif isinstance(self._model_summary, list) or isinstance(self._model_summary, dict):
            self._model_summary = JsonModelSummary(self._model_summary)

        self._algorithm_requirement = algorithm_requirement
        self._train_name = train_name
        self._train_version = train_version

    @property
    def data(self) -> dict:

        def with_ids(iterable, id_fun):
            return [{'id': id_fun(x), 'data': x[1].as_dict()} for x in iterable]
        properties = with_ids(self._properties.items(), id_fun=lambda x: x[0])
        formula = with_ids(enumerate(self._formula), id_fun=lambda x: x[0]+1)
        return {
            'trainVersion': self._train_version,
            'trainName': self._train_name,
            'descriptionVersion': '1.0',
            'properties': properties,
            'formula': formula,
            'model': {
                'summary': as_dict_or_none(self._model_summary)
            },
            'algorithm': {
                'requirement': as_dict_or_none(self._algorithm_requirement)
            }
        }

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'TrainDescription'
