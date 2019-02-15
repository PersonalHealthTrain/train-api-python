from pht.internal.response.describe.algorithm.FormulaAlgorithmRequirement import FormulaAlgorithmRequirement
from tests.base import BaseTest


class FormulaAlgorithmRequirementTests(BaseTest):

    def setUp(self):
        self.alg1 = FormulaAlgorithmRequirement(1)
        self.alg2 = FormulaAlgorithmRequirement(2)
        self.alg3 = FormulaAlgorithmRequirement(3)
        self.alg4 = FormulaAlgorithmRequirement(127)

    ################################################################################
    # Value Error
    ################################################################################
    def test_value_error_1(self):
        self.assertValueError(lambda: FormulaAlgorithmRequirement(0))

    def test_value_error_2(self):
        self.assertValueError(lambda: FormulaAlgorithmRequirement(-1))

    def test_value_error_3(self):
        self.assertValueError(lambda: FormulaAlgorithmRequirement(-10))

    ################################################################################
    # Type Error
    ################################################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: FormulaAlgorithmRequirement(None))

    def test_type_error_2(self):
        self.assertTypeError(lambda: FormulaAlgorithmRequirement(True))

    def test_type_error_3(self):
        self.assertTypeError(lambda: FormulaAlgorithmRequirement(False))

    def test_type_error_4(self):
        self.assertTypeError(lambda: FormulaAlgorithmRequirement('foo'))

    def test_type_error_5(self):
        self.assertTypeError(lambda: FormulaAlgorithmRequirement({}))

    def test_type_error_6(self):
        self.assertTypeError(lambda: FormulaAlgorithmRequirement([]))

    ################################################################################
    # Equal and hash
    ################################################################################
    def test_eq_hash_1(self):
        self.assertIsEqual(FormulaAlgorithmRequirement(1), self.alg1)

    def test_eq_hash_2(self):
        self.assertIsEqual(FormulaAlgorithmRequirement(2), self.alg2)

    def test_eq_hash_3(self):
        self.assertIsEqual(FormulaAlgorithmRequirement(3), self.alg3)

    def test_eq_hash_4(self):
        self.assertIsEqual(FormulaAlgorithmRequirement(127), self.alg4)

    def test_unequal(self):
        self.assertNotEqual(self.alg1, self.alg2)
        self.assertNotEqual(self.alg1, self.alg3)
        self.assertNotEqual(self.alg1, self.alg4)
        self.assertNotEqual(self.alg2, self.alg3)
        self.assertNotEqual(self.alg2, self.alg4)
        self.assertNotEqual(self.alg3, self.alg4)

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqual(self.alg1)

    def test_copy_2(self):
        self.assertCopiesAreEqual(self.alg2)

    def test_copy_3(self):
        self.assertCopiesAreEqual(self.alg3)

    def test_copy_4(self):
        self.assertCopiesAreEqual(self.alg4)

    ################################################################################
    # As Dict
    ################################################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={'formula_id': 1, 'type': 'FormulaAlgorithmRequirement', 'display': 'FormulaAlgorithmRequirement'},
            actual=self.alg1.as_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={'formula_id': 2, 'type': 'FormulaAlgorithmRequirement', 'display': 'FormulaAlgorithmRequirement'},
            actual=self.alg2.as_dict())

    def test_as_dict_3(self):
        self.checkExpect(
            expect={'formula_id': 3, 'type': 'FormulaAlgorithmRequirement', 'display': 'FormulaAlgorithmRequirement'},
            actual=self.alg3.as_dict())

    def test_as_dict_4(self):
        self.checkExpect(
            expect={'formula_id': 127, 'type': 'FormulaAlgorithmRequirement', 'display': 'FormulaAlgorithmRequirement'},
            actual=self.alg4.as_dict())

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg1.type)

    def test_type_2(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg2.type)

    def test_type_3(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg3.type)

    def test_type_4(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg4.type)

    ################################################################################
    # Display
    ################################################################################
    def test_dislay_1(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg1.display)

    def test_display_2(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg2.display)

    def test_display_3(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg3.display)

    def test_display_4(self):
        self.checkExpect(
            expect='FormulaAlgorithmRequirement',
            actual=self.alg4.display)

    ################################################################################
    # Data
    ################################################################################
    def test_data_1(self):
        self.checkExpect(
            expect={'formula_id': 1},
            actual=self.alg1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'formula_id': 2},
            actual=self.alg2.data)

    def test_data_3(self):
        self.checkExpect(
            expect={'formula_id': 3},
            actual=self.alg3.data)

    def test_data_4(self):
        self.checkExpect(
            expect={'formula_id': 127},
            actual=self.alg4.data)