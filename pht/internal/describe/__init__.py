import json
from typing import List
from .algorithm import AlgorithmRequirement
from .formula import Formula
from .property import Property


class TrainDescription:
    """
    Description of a train that is obtained when the train is invoked with the describe command
    """
    def __init__(self,
                 properties: List[Property],
                 formulas: List[Formula],
                 model_summary: str,
                 algorithm_requirement: AlgorithmRequirement):
        self._properties = properties
        self._formula = formulas
        self._model_summary = model_summary
        self._algorithm_requirement = algorithm_requirement

    def to_json_string(self) -> str:
        dictionary = {
            'properties': [prop.to_dict() for prop in self._properties],
            'formula': [f.to_dict() for f in self._formula],
            'model': {
                'summary': self._model_summary
            },
            'algorithm': {
                'requirement': self._algorithm_requirement.to_dict()
            }
        }
        return json.dumps(dictionary)
