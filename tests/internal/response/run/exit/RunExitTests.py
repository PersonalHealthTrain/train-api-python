"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
from tests.base import BaseTest
from pht.internal.response.run.exit.RunExit import AlgorithmApplicationRunExit, AlgorithmFailureRunExit, AlgorithmSuccessRunExit


class RunExitTests(BaseTest):

    def setUp(self):
        self.application = AlgorithmApplicationRunExit('app state')
        self.success = AlgorithmSuccessRunExit('success state')
        self.failure = AlgorithmFailureRunExit('failure state')
        self.application2 = AlgorithmApplicationRunExit(None)
        self.success2 = AlgorithmSuccessRunExit(None)
        self.failure2 = AlgorithmFailureRunExit(None)

    ################################################################################
    # eq and hash
    ################################################################################
    def test_eq_1(self):
        self.assertIsEqual(self.application, AlgorithmApplicationRunExit('app state'))

    def test_eq_2(self):
        self.assertIsEqual(self.success, AlgorithmSuccessRunExit('success state'))

    def test_eq_3(self):
        self.assertIsEqual(self.failure, AlgorithmFailureRunExit('failure state'))

    def test_eq_4(self):
        self.assertIsEqual(self.application2, AlgorithmApplicationRunExit(None))

    def test_eq_5(self):
        self.assertIsEqual(self.success2, AlgorithmSuccessRunExit(None))

    def test_eq_6(self):
        self.assertIsEqual(self.failure2, AlgorithmFailureRunExit(None))

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.application)

    def test_copy_2(self):
        self.assertCopiesAreEqualOf(self.failure)

    def test_copy_3(self):
        self.assertCopiesAreEqualOf(self.success)

    def test_copy_4(self):
        self.assertCopiesAreEqualOf(self.application2)

    def test_copy_5(self):
        self.assertCopiesAreEqualOf(self.failure2)

    def test_copy_6(self):
        self.assertCopiesAreEqualOf(self.success2)

    ################################################################################
    # as_dict
    ################################################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={
                '@type': ['AlgorithmSuccessRunExit', 'RunExit'],
                '@typeName': 'AlgorithmSuccessRunExit',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
                'state': 'success',
                'reason': 'success state'
            },
            actual=self.success.as_simple_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                '@type': ['AlgorithmFailureRunExit', 'RunExit'],
                '@typeName': 'AlgorithmFailureRunExit',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
                'state': 'failure',
                'reason': 'failure state'},
            actual=self.failure.as_simple_dict())

    def test_as_dict_3(self):
        self.checkExpect(
            expect={
                '@type': ['AlgorithmApplicationRunExit', 'RunExit'],
                '@typeName': 'AlgorithmApplicationRunExit',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
                'state': 'application',
                'reason': 'app state'
            },
            actual=self.application.as_simple_dict())

    def test_as_dict_4(self):
        self.checkExpect(
            expect={
                '@type': ['AlgorithmSuccessRunExit', 'RunExit'],
                '@typeName': 'AlgorithmSuccessRunExit',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
                'state': 'success',
                'reason': None
            },
            actual=self.success2.as_simple_dict())

    def test_as_dict_5(self):
        self.checkExpect(
            expect={
                '@type': ['AlgorithmFailureRunExit', 'RunExit'],
                '@typeName': 'AlgorithmFailureRunExit',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
                'state': 'failure',
                'reason': None},
            actual=self.failure2.as_simple_dict())

    def test_as_dict_6(self):
        self.checkExpect(
            expect={
                '@type': ['AlgorithmApplicationRunExit', 'RunExit'],
                '@typeName': 'AlgorithmApplicationRunExit',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
                'state': 'application',
                'reason': None
            },
            actual=self.application2.as_simple_dict())
