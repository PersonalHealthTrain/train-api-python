"""
Contains the RunAlgorithmResponse class, which belongs to the run_algorithm command.

@author Lukas Zimmermann
"""
from tests.base import BaseTest
from pht.internal.response.run.exit.RunExit import AlgorithmApplication, AlgorithmFailure, AlgorithmSuccess


class RunExitTests(BaseTest):

    def setUp(self):
        self.application = AlgorithmApplication('app state')
        self.success = AlgorithmSuccess('success state')
        self.failure = AlgorithmFailure('failure state')
        self.application2 = AlgorithmApplication(None)
        self.success2 = AlgorithmSuccess(None)
        self.failure2 = AlgorithmFailure(None)

    ################################################################################
    # eq and hash
    ################################################################################
    def test_eq_1(self):
        self.assertIsEqual(self.application, AlgorithmApplication('app state'))

    def test_eq_2(self):
        self.assertIsEqual(self.success, AlgorithmSuccess('success state'))

    def test_eq_3(self):
        self.assertIsEqual(self.failure, AlgorithmFailure('failure state'))

    def test_eq_4(self):
        self.assertIsEqual(self.application2, AlgorithmApplication(None))

    def test_eq_5(self):
        self.assertIsEqual(self.success2, AlgorithmSuccess(None))

    def test_eq_6(self):
        self.assertIsEqual(self.failure2, AlgorithmFailure(None))

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqual(self.application)

    def test_copy_2(self):
        self.assertCopiesAreEqual(self.failure)

    def test_copy_3(self):
        self.assertCopiesAreEqual(self.success)

    def test_copy_4(self):
        self.assertCopiesAreEqual(self.application2)

    def test_copy_5(self):
        self.assertCopiesAreEqual(self.failure2)

    def test_copy_6(self):
        self.assertCopiesAreEqual(self.success2)

    ################################################################################
    # as_dict
    ################################################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={'state': 'success', 'reason': 'success state'},
            actual=self.success.as_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={'state': 'failure', 'reason': 'failure state'},
            actual=self.failure.as_dict())

    def test_as_dict_3(self):
        self.checkExpect(
            expect={'state': 'application', 'reason': 'app state'},
            actual=self.application.as_dict())

    def test_as_dict_4(self):
        self.checkExpect(
            expect={'state': 'success', 'reason': None},
            actual=self.success2.as_dict())

    def test_as_dict_5(self):
        self.checkExpect(
            expect={'state': 'failure', 'reason': None},
            actual=self.failure2.as_dict())

    def test_as_dict_6(self):
        self.checkExpect(
            expect={'state': 'application', 'reason': None},
            actual=self.application2.as_dict())
