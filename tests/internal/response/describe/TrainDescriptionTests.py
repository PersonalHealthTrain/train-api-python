from tests.base import BaseTest
from pht.internal.response.describe.TrainDescription import TrainDescription
from pht.internal.response.describe.formula.Clause import Clause
from pht.internal.response.describe.formula.CNF import CNF
from pht.internal.response.describe.algorithm.FormulaAlgorithmRequirement import FormulaAlgorithmRequirement
from pht.internal.response.describe.property.environment_variable import enum_by_name, token_by_name, url_by_name


class TrainDescriptionTests(BaseTest):

    def setUp(self):
        self.td1 = TrainDescription(
            train_name='test_train',
            train_version='1.0',
            properties={
                1: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[CNF(Clause(1))],
            model_summary='model summary',
            algorithm_requirement=FormulaAlgorithmRequirement(1))

    ################################################################################
    # As Dict
    ################################################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={
                'trainName': 'test_train',
                'trainVersion': '1.0',
                'descriptionVersion': '1.0',
                'properties': [
                    {
                        'id': 1,
                        'data': {
                            'description': None,
                            'target': 'http://schema.org/URL',
                            'name': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            }, 'type': 'http://www.wikidata.org/entity/Q400857',
                            'display': 'environmentVariable'
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'description': None,
                            'target': 'token',
                            'name': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            'type': 'http://www.wikidata.org/entity/Q400857',
                            'display': 'environmentVariable'
                        }
                    },
                    {''
                     'id': 3,
                     'data': {
                         'description': None,
                         'target': 'enum',
                         'name': 'BAZ',
                         'state': {
                             'isAvailable': False,
                             'reason': "Environment variable 'BAZ' not set"
                         },
                         'choices': ['VALUE1', 'VALUE2'],
                         'type': 'http://www.wikidata.org/entity/Q400857',
                         'display': 'environmentVariable'
                     }
                     }
                ],
                'formula': [
                    {'id': 1,
                     'data': {
                         'value': [[1]],
                         'type': 'https://www.wikidata.org/wiki/Q846564',
                         'display': 'ConjunctiveNormalForm'
                     }
                     }
                ],
                'model':
                    {
                        'summary': {
                            'type': 'StringModelSummary',
                            'display': 'StringModelSummary',
                            'value': 'model summary'
                        }
                    },
                'algorithm': {
                    'requirement':
                        {
                            'formula_id': 1,
                            'type': 'FormulaAlgorithmRequirement',
                            'display': 'FormulaAlgorithmRequirement'
                        }
                },
                'type': 'TrainDescription', 'display': 'TrainDescription'}, actual=self.td1.as_dict())

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect='TrainDescription',
            actual=self.td1.type
        )

    ################################################################################
    # Display
    ################################################################################
    def test_display_1(self):
        self.checkExpect(
            expect='TrainDescription',
            actual=self.td1.display
        )

    ################################################################################
    # Data
    ################################################################################
    def test_data_1(self):
        self.checkExpect(
            expect={
                'trainVersion': '1.0',
                'trainName': 'test_train',
                'descriptionVersion': '1.0',
                'properties': [
                    {
                        'id': 1,
                        'data': {
                            'description': None,
                            'target': 'http://schema.org/URL',
                            'name': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            },
                            'type': 'http://www.wikidata.org/entity/Q400857',
                            'display': 'environmentVariable'
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'description': None,
                            'target': 'token',
                            'name': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            'type': 'http://www.wikidata.org/entity/Q400857',
                            'display': 'environmentVariable'
                        }
                    },
                    {
                        'id': 3,
                        'data':
                            {
                                'description': None,
                                'target': 'enum',
                                'name': 'BAZ',
                                'state': {
                                    'isAvailable': False,
                                    'reason': "Environment variable 'BAZ' not set"
                                },
                                'choices': ['VALUE1', 'VALUE2'],
                                'type': 'http://www.wikidata.org/entity/Q400857',
                                'display': 'environmentVariable'
                            }
                    }
                ],
                'formula': [
                    {'id': 1,
                     'data': {'value': [[1]],
                              'type': 'https://www.wikidata.org/wiki/Q846564',
                              'display': 'ConjunctiveNormalForm'
                              }
                     }
                ],
                'model': {
                    'summary': {
                        'type': 'StringModelSummary',
                        'display': 'StringModelSummary',
                        'value': 'model summary'
                    }
                },
                'algorithm': {
                    'requirement': {
                        'formula_id': 1,
                        'type': 'FormulaAlgorithmRequirement',
                        'display': 'FormulaAlgorithmRequirement'}}},
            actual=self.td1.data
        )
