from tests.base import BaseTest
from pht.internal.response.describe.TrainDescription import TrainDescription
from pht.internal.response.describe.formula.Clause import Clause
from pht.internal.response.describe.formula.CNF import ConjunctiveNormalForm
from pht.internal.response.describe.algorithm.FormulaAlgorithmRequirement import FormulaAlgorithmRequirement
from pht.internal.response.describe.property.environment_variable import enum_by_name, token_by_name, url_by_name


class TrainDescriptionTests(BaseTest):

    def setUp(self):
        self.maxDiff = None
        self.td1 = TrainDescription(
            train_name='test_train',
            train_version='1.0',
            properties={
                1: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[ConjunctiveNormalForm(Clause(1))],
            model_summary='model summary',
            algorithm_requirement=FormulaAlgorithmRequirement(1))

        self.td2 = TrainDescription(
            train_name='test_train',
            train_version='1.0',
            properties={
                1: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[ConjunctiveNormalForm(Clause(1))],
            model_summary='model summary',
            algorithm_requirement=None)

        self.td3 = TrainDescription(
            train_name='test_train',
            train_version='1.0',
            properties={
                1: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[
                ConjunctiveNormalForm(
                    Clause(1), Clause(-2, 1, 3), Clause(3, 1, -2, -3)
                ),
                ConjunctiveNormalForm(
                    Clause(3, 1), Clause(2, 1, 3, -3)
                ),
                ConjunctiveNormalForm(
                    Clause(-1)
                )
            ],
            model_summary='model summary',
            algorithm_requirement=FormulaAlgorithmRequirement(3))

    ################################################################################
    # These Train Descriptions are invalid
    ################################################################################

    # FormulaAlgorithmRequirement points to a formula which is not there
    def test_invalid_train_description_1(self):
        self.assertValueError(lambda: TrainDescription(
                train_name='foo',
                train_version='1.0',
                properties={
                    1: url_by_name('FOO'),
                    2: token_by_name('BAR'),
                    3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
                },
                formulas=[],
                model_summary='model summary',
                algorithm_requirement=FormulaAlgorithmRequirement(1)))

    # Formula Algorithm Requirement points to a meaningless value
    def test_invalid_train_description_2(self):
        self.assertValueError(lambda: TrainDescription(
            train_name='foo',
            train_version='1.0',
            properties={
                1: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[],
            model_summary='model summary',
            algorithm_requirement=FormulaAlgorithmRequirement(-1)))

    # Property number '-1' is invalid
    def test_invalid_train_description_3(self):
        self.assertValueError(lambda: TrainDescription(
            train_name='foo',
            train_version='1.0',
            properties={
                -1: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[],
            model_summary='model summary',
            algorithm_requirement=None))

    # Property number '0' is invalid
    def test_invalid_train_description_4(self):
        self.assertValueError(lambda: TrainDescription(
            train_name='foo',
            train_version='1.0',
            properties={
                0: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[],
            model_summary='model summary',
            algorithm_requirement=None))

    # There is at least one formula which uses a property which does not exist
    def test_invalid_train_description_5(self):
        self.assertValueError(lambda: TrainDescription(
            train_name='foo',
            train_version='1.0',
            properties={
                1: url_by_name('FOO'),
                2: token_by_name('BAR'),
                3: enum_by_name('BAZ', choices=['VALUE1', 'VALUE2'])
            },
            formulas=[
                ConjunctiveNormalForm(
                    Clause(1, -3), Clause(4),
                )
            ],
            model_summary='model summary',
            algorithm_requirement=None))

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
                            'description': '',
                            'environmentVariableName': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            },
                            '@type': ['UrlEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'UrlEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            '@type': ['TokenEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'TokenEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {''
                     'id': 3,
                     'data': {
                         'description': '',
                         'environmentVariableName': 'BAZ',
                         'state': {
                             'isAvailable': False,
                             'reason': "Environment variable 'BAZ' not set"
                         },
                         'choices': ['VALUE1', 'VALUE2'],
                         '@type':  ['EnumEnvironmentVariableProperty',
                                    'EnvironmentVariableProperty',
                                    'Property'],
                         '@typeName': 'EnumEnvironmentVariableProperty',
                         '@typeSystem': {
                            'name': 'pythonclass',
                            'version': '1.0'
                         }
                     }
                    }
                ],
                'formula': [
                    {
                        'id': 1,
                        'data': {
                            'value': [[1]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'model':
                    {
                        'summary': {
                            '@type': ['StringModelSummary', 'ModelSummary'],
                            '@typeName': 'StringModelSummary',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            },
                            'value': 'model summary'
                        }
                    },
                'algorithm': {
                    'requirement':
                        {
                            'formula_id': 1,
                            '@type': ['FormulaAlgorithmRequirement',
                                      'AlgorithmRequirement'],
                            '@typeName': 'FormulaAlgorithmRequirement',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                },
                '@type': ['TrainDescription', 'TrainResponse'],
                '@typeName': 'TrainDescription',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                }
            }, actual=self.td1._as_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'trainVersion': '1.0',
                'trainName': 'test_train',
                'descriptionVersion': '1.0',
                'properties': [
                    {
                        'id': 1,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            },
                            '@type': ['UrlEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'UrlEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            '@type': ['TokenEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'TokenEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 3,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAZ',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAZ' not set"
                            },
                            'choices': ['VALUE1', 'VALUE2'],
                            '@type':  ['EnumEnvironmentVariableProperty',
                                       'EnvironmentVariableProperty',
                                       'Property'],
                            '@typeName': 'EnumEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ], 'formula': [
                    {
                        'id': 1,
                        'data': {
                            'value': [[1]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'model': {
                    'summary': {
                        'value': 'model summary',
                        '@type': ['StringModelSummary', 'ModelSummary'],
                        '@typeName': 'StringModelSummary',
                        '@typeSystem': {
                            'name': 'pythonclass',
                            'version': '1.0'
                        }
                    }
                }, 'algorithm': {
                    'requirement': None
                },
                '@type': ['TrainDescription', 'TrainResponse'],
                '@typeName': 'TrainDescription',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                }
            },
            actual=self.td2.as_simple_dict())

    def test_as_dict_3(self):
        self.checkExpect(
            expect={
                'trainVersion': '1.0',
                'trainName': 'test_train',
                'descriptionVersion': '1.0',
                'properties': [
                    {
                        'id': 1,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            },
                            '@type': ['UrlEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'UrlEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                    , {
                        'id': 2,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            '@type': ['TokenEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'TokenEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 3,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAZ',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAZ' not set"
                            },
                            'choices': ['VALUE1', 'VALUE2'],
                            '@type':  ['EnumEnvironmentVariableProperty',
                                       'EnvironmentVariableProperty',
                                       'Property'],
                            '@typeName': 'EnumEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'formula': [
                    {
                        'id': 1,
                        'data': {
                            'value': [[-3, -2, 1, 3], [-2, 1, 3], [1]],
                            '@type':  ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'value': [[-3, 1, 2, 3], [1, 3]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 3,
                        'data': {
                            'value': [[-1]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'model': {
                    'summary': {
                        'value': 'model summary',
                        '@type': ['StringModelSummary', 'ModelSummary'],
                        '@typeName': 'StringModelSummary',
                        '@typeSystem': {
                            'name': 'pythonclass',
                            'version': '1.0'
                        }
                    }
                },
                'algorithm': {
                    'requirement': {
                        'formula_id': 3,
                        '@type': ['FormulaAlgorithmRequirement',
                                  'AlgorithmRequirement'],
                        '@typeName': 'FormulaAlgorithmRequirement',
                        '@typeSystem': {
                            'name': 'pythonclass',
                            'version': '1.0'
                        }
                    }
                },
                '@type': ['TrainDescription', 'TrainResponse'],
                '@typeName': 'TrainDescription',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                }
            },
            actual=self.td3.as_simple_dict())

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['TrainDescription', 'TrainResponse'],
            actual=self.td1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['TrainDescription', 'TrainResponse'],
            actual=self.td2.type)

    def test_type_3(self):
        self.checkExpect(
            expect=['TrainDescription', 'TrainResponse'],
            actual=self.td3.type)

    ################################################################################
    # Display
    ################################################################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='TrainDescription',
            actual=self.td1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='TrainDescription',
            actual=self.td2.type_name)

    def test_type_name_3(self):
        self.checkExpect(
            expect='TrainDescription',
            actual=self.td3.type_name)

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
                            'description': '',
                            'environmentVariableName': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            },
                            '@type': ['UrlEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'UrlEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            '@type': ['TokenEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'TokenEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 3,
                        'data':
                            {
                                'description': '',
                                'environmentVariableName': 'BAZ',
                                'state': {
                                    'isAvailable': False,
                                    'reason': "Environment variable 'BAZ' not set"
                                },
                                'choices': ['VALUE1', 'VALUE2'],
                                '@type':  ['EnumEnvironmentVariableProperty',
                                           'EnvironmentVariableProperty',
                                           'Property'],
                                '@typeName': 'EnumEnvironmentVariableProperty',
                                '@typeSystem': {
                                    'name': 'pythonclass',
                                    'version': '1.0'
                                }
                            }
                    }
                ],
                'formula': [
                    {
                        'id': 1,
                        'data': {
                            'value': [[1]],
                            '@type':  ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                     }
                ],
                'model': {
                    'summary': {
                        '@type': ['StringModelSummary', 'ModelSummary'],
                        '@typeName': 'StringModelSummary',
                        '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                         },
                        'value': 'model summary'
                    }
                },
                'algorithm': {
                    'requirement': {
                        'formula_id': 1,
                        '@type': ['FormulaAlgorithmRequirement',
                                  'AlgorithmRequirement'],
                        '@typeName': 'FormulaAlgorithmRequirement',
                        '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                    }
                }
            },
            actual=self.td1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={
                'trainVersion': '1.0',
                'trainName': 'test_train',
                'descriptionVersion': '1.0',
                'properties': [
                    {
                        'id': 1,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            },
                            '@type': ['UrlEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'UrlEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            '@type': ['TokenEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'TokenEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 3,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAZ',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAZ' not set"
                            },
                            'choices': ['VALUE1', 'VALUE2'],
                            '@type': ['EnumEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'EnumEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'formula': [
                    {
                        'id': 1,
                        'data': {
                            'value': [[1]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'model': {
                    'summary': {
                        'value': 'model summary',
                        '@type': ['StringModelSummary', 'ModelSummary'],
                        '@typeName': 'StringModelSummary',
                        '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                    }
                }, 'algorithm': {'requirement': None}
            },
            actual=self.td2.data)

    def test_data_3(self):
        self.checkExpect(
            expect={
                'trainVersion': '1.0',
                'trainName': 'test_train',
                'descriptionVersion': '1.0',
                'properties': [
                    {
                        'id': 1,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'FOO',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'FOO' not set"
                            },
                            '@type': ['UrlEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'UrlEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAR',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAR' not set"
                            },
                            '@type': ['TokenEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'TokenEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }, {
                        'id': 3,
                        'data': {
                            'description': '',
                            'environmentVariableName': 'BAZ',
                            'state': {
                                'isAvailable': False,
                                'reason': "Environment variable 'BAZ' not set"
                            },
                            'choices': ['VALUE1', 'VALUE2'],
                            '@type': ['EnumEnvironmentVariableProperty',
                                      'EnvironmentVariableProperty',
                                      'Property'],
                            '@typeName': 'EnumEnvironmentVariableProperty',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'formula': [
                    {
                        'id': 1,
                        'data': {
                            'value': [[-3, -2, 1, 3], [-2, 1, 3], [1]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 2,
                        'data': {
                            'value': [[-3, 1, 2, 3], [1, 3]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    },
                    {
                        'id': 3,
                        'data': {
                            'value': [[-1]],
                            '@type': ['ConjunctiveNormalForm', 'Formula'],
                            '@typeName': 'ConjunctiveNormalForm',
                            '@typeSystem': {
                                'name': 'pythonclass',
                                'version': '1.0'
                            }
                        }
                    }
                ],
                'model': {
                    'summary': {
                        'value': 'model summary',
                        '@type': ['StringModelSummary', 'ModelSummary'],
                        '@typeName': 'StringModelSummary',
                        '@typeSystem': {
                            'name': 'pythonclass',
                            'version': '1.0'
                        }
                    }
                },
                'algorithm': {
                    'requirement': {
                        'formula_id': 3,
                        '@type': ['FormulaAlgorithmRequirement', 'AlgorithmRequirement'],
                        '@typeName': 'FormulaAlgorithmRequirement',
                        '@typeSystem': {
                            'name': 'pythonclass',
                            'version': '1.0'
                        }
                    }
                }
            },
            actual=self.td3.data)
