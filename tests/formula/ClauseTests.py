import unittest
from pht.formula import Clause


class ClauseTests(unittest.TestCase):

    def setUp(self):
        self.clause1 = Clause(1)
        self.clause2 = Clause(-1)
        self.clause3 = Clause(1, 2)
        self.clause4 = Clause(-1, 2)
        self.clause5 = Clause(1, -2)
        self.clause6 = Clause(-1, -2)

    ################################################################################
    # Empty Clause is not allowed
    ################################################################################
    def test_empty_clause(self):
        with(self.assertRaises(TypeError)):
            Clause()

    ################################################################################
    # Zero is not allowed as a literal
    ################################################################################
    def test_zero_not_allowed_1(self):
        with(self.assertRaises(ValueError)):
            Clause(0)

    def test_zero_not_allowed_2(self):
        with(self.assertRaises(ValueError)):
            Clause(0, 1)

    def test_zero_not_allowed_3(self):
        with(self.assertRaises(ValueError)):
            Clause(0, -1)

    def test_zero_not_allowed_4(self):
        with(self.assertRaises(ValueError)):
            Clause(0, -1, 2)

    ################################################################################
    # Iter
    ################################################################################
    def test_iter_1(self):
        clause = self.clause1
        self.assertIn(1, clause)
        self.assertNotIn(2, clause)

    def test_iter_2(self):
        clause = self.clause2
        self.assertIn(-1, clause)
        self.assertNotIn(1, clause)

    def test_iter_3(self):
        clause = self.clause3
        self.assertIn(1, clause)
        self.assertIn(2, clause)
        self.assertNotIn(-1, clause)
        self.assertNotIn(-2, clause)
        self.assertNotIn(0, clause)
        self.assertNotIn(117, clause)

    def test_iter_4(self):
        clause = self.clause4
        self.assertIn(-1, clause)
        self.assertIn(2, clause)
        self.assertNotIn(1, clause)
        self.assertNotIn(-2, clause)
        self.assertNotIn(0, clause)
        self.assertNotIn(-5, clause)

    def test_iter_5(self):
        clause = self.clause5
        self.assertIn(1, clause)
        self.assertIn(-2, clause)
        self.assertNotIn(-1, clause)
        self.assertNotIn(2, clause)
        self.assertNotIn(0, clause)
        self.assertNotIn(-17, clause)

    def test_iter_6(self):
        clause = self.clause6
        self.assertIn(-1, clause)
        self.assertIn(-2, clause)
        self.assertNotIn(1, clause)
        self.assertNotIn(2, clause)
        self.assertNotIn(0, clause)
        self.assertNotIn(255, clause)

    ################################################################################
    # Equals
    ################################################################################
    def test_ident_implies_equals(self):
        self.assertEqual(self.clause1, self.clause1)
        self.assertEqual(self.clause2, self.clause2)
        self.assertEqual(self.clause3, self.clause3)
        self.assertEqual(self.clause4, self.clause4)
        self.assertEqual(self.clause5, self.clause5)
        self.assertEqual(self.clause6, self.clause6)

    def test_equal_1(self):
        x = Clause(1)
        y = Clause(1)
        self.assertEqual(x, y)
        self.assertIsNot(x, y)

    def test_equal_2(self):
        x = Clause(-1)
        y = Clause(-1)
        self.assertEqual(x, y)
        self.assertIsNot(x, y)

    def test_equal_3(self):
        x = Clause(-5, 3)
        y = Clause(-5, 3)
        self.assertEqual(x, y)
        self.assertIsNot(x, y)

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        c1 = Clause(1)
        c2 = c1.copy()
        self.assertEqual(c1, c2)
        self.assertIsNot(c1, c2)

    def test_copy_2(self):
        c1 = Clause(1, -3)
        c2 = c1.copy()
        self.assertEqual(c1, c2)
        self.assertIsNot(c1, c2)
