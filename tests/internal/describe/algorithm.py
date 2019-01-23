from pht.internal.describe.algorithm import FormulaAlgorithmRequirement
from tests.base import BaseTest
from copy import copy, deepcopy


class AlgorithmTests(BaseTest):

    def setUp(self):
        self.alg1 = FormulaAlgorithmRequirement(1)
        self.alg2 = FormulaAlgorithmRequirement(2)
        self.alg3 = FormulaAlgorithmRequirement(3)
        self.alg4 = FormulaAlgorithmRequirement(127)

    ################################################################################
    # Invalid constructor arguments (invalid ids)
    ################################################################################
    def test_invalid_id_1(self):

        with self.assertRaises(ValueError):
            FormulaAlgorithmRequirement(0)

    def test_invalid_id_2(self):
        with self.assertRaises(ValueError):
            FormulaAlgorithmRequirement(-1)

    def test_invalid_id_3(self):
        with self.assertRaises(TypeError):
            FormulaAlgorithmRequirement(None)

    def test_invalid_id_4(self):
        with self.assertRaises(TypeError):
            FormulaAlgorithmRequirement(True)

    def test_invalid_5(self):
        with self.assertRaises(TypeError):
            FormulaAlgorithmRequirement('foo')

    def test_invalid_6(self):
        with self.assertRaises(TypeError):
            FormulaAlgorithmRequirement({})

    def test_invalid_7(self):
        with self.assertRaises(TypeError):
            FormulaAlgorithmRequirement([])

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
            expect={'value': 1},
            actual=self.alg1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'value': 2},
            actual=self.alg2.data)

    def test_data_3(self):
        self.checkExpect(
            expect={'value': 3},
            actual=self.alg3.data)

    def test_data_4(self):
        self.checkExpect(
            expect={'value': 127},
            actual=self.alg4.data)

    ################################################################################
    # Equal and hash
    ################################################################################
    def test_eq_1(self):
        c = FormulaAlgorithmRequirement(1)
        self.assertEqual(c, self.alg1)
        self.assertEqual(hash(c), hash(self.alg1))

    def test_eq_2(self):
        c = FormulaAlgorithmRequirement(2)
        self.assertEqual(c, self.alg2)
        self.assertEqual(hash(c), hash(self.alg2))

    def test_eq_3(self):
        c = FormulaAlgorithmRequirement(3)
        self.assertEqual(c, self.alg3)
        self.assertEqual(hash(c), hash(self.alg3))

    def test_eq_4(self):
        c = FormulaAlgorithmRequirement(127)
        self.assertEqual(c, self.alg4)
        self.assertEqual(hash(c), hash(self.alg4))

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        c1 = copy(self.alg1)
        c2 = deepcopy(self.alg1)
        c3 = self.alg1.copy()
        self.assertEqual(c1, self.alg1)
        self.assertEqual(c2, self.alg1)
        self.assertEqual(c3, self.alg1)

    def test_copy_2(self):
        c1 = copy(self.alg2)
        c2 = deepcopy(self.alg2)
        c3 = self.alg2.copy()
        self.assertEqual(c1, self.alg2)
        self.assertEqual(c2, self.alg2)
        self.assertEqual(c3, self.alg2)

    def test_copy_3(self):
        c1 = copy(self.alg3)
        c2 = deepcopy(self.alg3)
        c3 = self.alg3.copy()
        self.assertEqual(c1, self.alg3)
        self.assertEqual(c2, self.alg3)
        self.assertEqual(c3, self.alg3)

    def test_copy_4(self):
        c1 = copy(self.alg4)
        c2 = deepcopy(self.alg4)
        c3 = self.alg4.copy()
        self.assertEqual(c1, self.alg4)
        self.assertEqual(c2, self.alg4)
        self.assertEqual(c3, self.alg4)

