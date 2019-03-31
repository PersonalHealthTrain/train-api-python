from typing import Dict, List, Optional, Union
from pht.internal.response.TrainResponse import TrainResponse
from pht.internal.response.describe.property.Property import Property
from pht.internal.response.describe.formula.Formula import Formula
from pht.internal.response.describe.algorithm.AlgorithmRequirement import AlgorithmRequirement
from pht.internal.response.describe.algorithm.FormulaAlgorithmRequirement import FormulaAlgorithmRequirement
from pht.internal.response.describe.model.ModelSummary import ModelSummary
from pht.internal.response.describe.model.StringModelSummary import StringModelSummary
from pht.internal.response.describe.model.JsonModelSummary import JsonModelSummary
from pht.internal.util.misc import as_dict_or_none, copy_or_none
from pht.internal.util import require
from pht.internal.util.builder import copy_property_map
from pht.internal.util.predicate.maker import is_in_closed_range
from pht.internal.util.predicate import is_positive
from pht.internal.response.describe.formula.CNF import ConjunctiveNormalForm


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

        # Initialize and validate individual fields of the TrainDescription
        self._train_name = train_name
        self._train_version = train_version

        self._properties = copy_property_map(properties)
        self._validate_property_map()

        self._formulas = [formula.deepcopy() for formula in formulas]
        self._algorithm_requirement = copy_or_none(algorithm_requirement)
        self._validate_formula_algorithm_requirement()

        self._model_summary = TrainDescription._create_model_summary(model_summary)

        self._validate_literals_in_formulas()

    def deepcopy(self):
        return TrainDescription(
            train_name=self._train_name,
            train_version=self._train_version,
            properties=self._properties,
            formulas=self._formulas,
            model_summary=self._model_summary,
            algorithm_requirement=self._algorithm_requirement)

    def __hash__(self):
        # TODO Useful hash function
        return 1

    @property
    def data(self) -> dict:

        def with_ids(iterable, id_fun):
            return [{'id': id_fun(x), 'data': x[1].as_simple_mapping()} for x in iterable]
        properties = with_ids(self._properties.items(), id_fun=lambda x: x[0])
        formula = with_ids(enumerate(self._formulas), id_fun=lambda x: x[0] + 1)
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

    @staticmethod
    def _create_model_summary(model_summary: Union[ModelSummary, str, dict, list, None]):
        """
        Translates the input to a ModelSummary instance
        """
        if isinstance(model_summary, str):
            return StringModelSummary(model_summary)
        elif isinstance(model_summary, list) or isinstance(model_summary, dict):
            return JsonModelSummary(model_summary)
        return model_summary.deepcopy()

    def _validate_formula_algorithm_requirement(self):
        """
        Checks that a potential FormulaAlgorithmRequirement points to an existing formula
        """
        if isinstance(self._algorithm_requirement, FormulaAlgorithmRequirement):
            formula_id = self._algorithm_requirement.data['formula_id']
            require.for_value(formula_id,
                              that=is_in_closed_range(1, len(self._formulas)),
                              error_if_not='No such formula: {}'.format(formula_id))

    def _validate_property_map(self):
        """
        Checks that all Property numbers are positive (otherwise they could not be literals in the formula)
        """
        require.for_each_value(
            inside=self._properties.keys(),
            that=is_positive,
            error_if_not='Property Number {} is not positive!')

    def _validate_literals_in_formulas(self):
        prop_keys = set(self._properties.keys())
        literals = {abs(literal)
                    for formula in self._formulas
                    for clause in formula
                    for literal in clause if isinstance(formula, ConjunctiveNormalForm)}
        require.that(
            literals.issubset(prop_keys),
            error_if_not='There are literals in the formula that are not declared as properties!')
