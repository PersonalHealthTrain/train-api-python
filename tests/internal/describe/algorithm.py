import unittest
from pht.internal.describe.algorithm import FormulaAlgorithmRequirement


class AlgorithmTests(unittest.TestCase):

    def setUp(self):
        self.alg1 = FormulaAlgorithmRequirement(1)
        self.alg2 = FormulaAlgorithmRequirement(2)
        self.alg3 = FormulaAlgorithmRequirement(3)
    #
    # def test_something(self):
    #     self.assertEqual(True, False)
