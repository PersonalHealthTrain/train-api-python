import unittest
from copy import copy, deepcopy
from pht.internal import Clause


class ClauseTests(unittest.TestCase):

    def setUp(self):
        self.clause1 = Clause(1)
        self.clause2 = Clause(-1)
        self.clause3 = Clause(1, 2)
        self.clause4 = Clause(-1, 2)
        self.clause5 = Clause(1, -2)
        self.clause6 = Clause(-1, -2)

    ################################################################################
    # Invalid Argument in C'tor
    ################################################################################
    def test_invalid_arg_ctor_1(self):
        with self.assertRaises(TypeError):
            Clause('foo')

    def test_invalid_arg_ctor_2(self):
        with self.assertRaises(TypeError):
            Clause(True)

    def test_invalid_arg_ctor_3(self):
        with self.assertRaises(TypeError):
            Clause({})

    def test_invalid_arg_ctor_4(self):
        with self.assertRaises(TypeError):
            Clause([])

    def test_invalid_arg_ctor_5(self):
        with self.assertRaises(TypeError):
            Clause(1.4)

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
        self.assertEqual(hash(x), hash(y))

    def test_equal_2(self):
        x = Clause(-1)
        y = Clause(-1)
        self.assertEqual(x, y)
        self.assertIsNot(x, y)
        self.assertEqual(hash(x), hash(y))

    def test_equal_3(self):
        x = Clause(-5, 3)
        y = Clause(-5, 3)
        self.assertEqual(x, y)
        self.assertIsNot(x, y)
        self.assertEqual(hash(x), hash(y))

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        c1 = Clause(1)
        c2 = c1.copy()
        self.assertEqual(c1, c2)
        self.assertIsNot(c1, c2)
        self.assertEqual(hash(c1), hash(c2))

    def test_copy_2(self):
        c1 = Clause(1, -3)
        c2 = c1.copy()
        self.assertEqual(c1, c2)
        self.assertIsNot(c1, c2)
        self.assertEqual(hash(c1), hash(c2))

    def test_copy_3(self):
        c1 = Clause(1, 2)
        c2 = copy(c1)
        self.assertEqual(c1, c2)
        self.assertIsNot(c1, c2)
        self.assertEqual(hash(c1), hash(c2))

    def test_copy_4(self):
        c1 = Clause(-1, 10)
        c2 = deepcopy(c1)
        self.assertEqual(c1, c2)
        self.assertIsNot(c1, c2)
        self.assertEqual(hash(c1), hash(c2))

    ################################################################################
    # str
    ################################################################################
    def test_str_1(self):
        self.assertEqual('[1]', str(self.clause1))

    def test_str_2(self):
        self.assertEqual('[-1]', str(self.clause2))

    def test_str_3(self):
        self.assertEqual('[1, 2]', str(self.clause3))

    def test_str_4(self):
        self.assertEqual('[-1, 2]', str(self.clause4))

    def test_str_5(self):
        self.assertEqual('[-2, 1]', str(self.clause5))

    def test_str_6(self):
        self.assertEqual('[-2, -1]', str(self.clause6))

    ################################################################################
    # repr
    ################################################################################
    def test_repr_1(self):
        self.assertEqual('[1]', repr(self.clause1))

    def test_repr_2(self):
        self.assertEqual('[-1]', repr(self.clause2))

    def test_repr_3(self):
        self.assertEqual('[1, 2]', repr(self.clause3))

    def test_repr_4(self):
        self.assertEqual('[-1, 2]', repr(self.clause4))

    def test_repr_5(self):
        self.assertEqual('[-2, 1]', repr(self.clause5))

    def test_repr_6(self):
        self.assertEqual('[-2, -1]', repr(self.clause6))

    ################################################################################
    # contains
    ################################################################################
    def test_contains_1(self):
        self.assertIn(1, self.clause1)

    def test_contains_2(self):
        self.assertIn(-1, self.clause2)
        self.assertNotIn(1, self.clause2)

    def test_contains_3(self):
        self.assertIn(1, self.clause3)
        self.assertIn(2, self.clause3)
        self.assertNotIn(-1, self.clause3)
        self.assertNotIn(-2, self.clause3)

    def test_contains_4(self):
        self.assertIn(-1, self.clause4)
        self.assertIn(2, self.clause4)
        self.assertNotIn(1, self.clause4)
        self.assertNotIn(-2, self.clause4)

    def test_contains_5(self):
        self.assertIn(1, self.clause5)
        self.assertIn(-2, self.clause5)
        self.assertNotIn(-1, self.clause5)
        self.assertNotIn(2, self.clause5)

    def test_contains_6(self):
        self.assertIn(-1, self.clause6)
        self.assertIn(-2, self.clause6)
        self.assertNotIn(1, self.clause6)
        self.assertNotIn(2, self.clause6)

    ################################################################################
    # len
    ################################################################################
    def test_len_1(self):
        self.assertEqual(1, len(self.clause1))

    def test_len_2(self):
        self.assertEqual(1, len(self.clause2))

    def test_len_3(self):
        self.assertEqual(2, len(self.clause3))

    def test_len_4(self):
        self.assertEqual(2, len(self.clause4))

    def test_len_5(self):
        self.assertEqual(2, len(self.clause5))

    def test_len_6(self):
        self.assertEqual(2, len(self.clause6))
