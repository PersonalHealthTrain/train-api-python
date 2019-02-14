from tests.base import BaseTest
from pht.internal.response.describe.formula.Clause import Clause


class ClauseTests(BaseTest):

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
        self.assertTypeError(lambda: Clause())

    ################################################################################
    # Value Error
    ################################################################################
    def test_value_error_1(self):
        self.assertValueError(lambda: Clause(0))

    def test_value_error_2(self):
        self.assertValueError(lambda: Clause(0, 1))

    def test_value_error_3(self):
        self.assertValueError(lambda: Clause(0, -1))

    def test_value_error_4(self):
        self.assertValueError(lambda: Clause(0, -1, 2))

    ################################################################################
    # Type Error
    ################################################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: Clause('foo'))

    def test_type_error_2(self):
        self.assertTypeError(lambda: Clause(True))

    def test_type_error_3(self):
        self.assertTypeError(lambda: Clause({}))

    def test_type_error_4(self):
        self.assertTypeError(lambda: Clause([]))

    def test_type_error_5(self):
        self.assertTypeError(lambda: Clause(1.4))

    def test_type_error_6(self):
        self.assertTypeError(lambda: Clause(None))

    ################################################################################
    # Equals and hash
    ################################################################################
    def test_eq_hash_1(self):
        self.assertIsEqual(Clause(1), self.clause1)

    def test_eq_hash_2(self):
        self.assertIsEqual(Clause(-1), self.clause2)

    def test_eq_hash_3(self):
        self.assertIsEqual(Clause(1, 2), self.clause3)

    def test_eq_hash_4(self):
        self.assertIsEqual(Clause(-1, 2), self.clause4)

    def test_eq_hash_5(self):
        self.assertIsEqual(Clause(1, -2), self.clause5)

    def test_eq_hash_6(self):
        self.assertIsEqual(Clause(-1, -2), self.clause6)

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqual(self.clause1)

    def test_copy_2(self):
        self.assertCopiesAreEqual(self.clause2)

    def test_copy_3(self):
        self.assertCopiesAreEqual(self.clause3)

    def test_copy_4(self):
        self.assertCopiesAreEqual(self.clause4)

    def test_copy_5(self):
        self.assertCopiesAreEqual(self.clause5)

    def test_copy_6(self):
        self.assertCopiesAreEqual(self.clause6)

    ################################################################################
    # iter
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
    # str
    ################################################################################
    def test_str_1(self):
        self.checkExpect(
            expect='[1]',
            actual=str(self.clause1))

    def test_str_2(self):
        self.checkExpect(
            expect='[-1]',
            actual=str(self.clause2))

    def test_str_3(self):
        self.checkExpect(
            expect='[1, 2]',
            actual=str(self.clause3))

    def test_str_4(self):
        self.checkExpect(
            expect='[-1, 2]',
            actual=str(self.clause4))

    def test_str_5(self):
        self.checkExpect(
            expect='[-2, 1]',
            actual=str(self.clause5))

    def test_str_6(self):
        self.checkExpect(
            expect='[-2, -1]',
            actual=str(self.clause6))

    ################################################################################
    # repr
    ################################################################################
    def test_repr_1(self):
        self.checkExpect(
            expect='[1]',
            actual=repr(self.clause1))

    def test_repr_2(self):
        self.checkExpect(
            expect='[-1]',
            actual=repr(self.clause2))

    def test_repr_3(self):
        self.checkExpect(
            expect='[1, 2]',
            actual=repr(self.clause3))

    def test_repr_4(self):
        self.checkExpect(
            expect='[-1, 2]',
            actual=repr(self.clause4))

    def test_repr_5(self):
        self.checkExpect(
            expect='[-2, 1]',
            actual=repr(self.clause5))

    def test_repr_6(self):
        self.checkExpect(
            expect='[-2, -1]',
            actual=repr(self.clause6))

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
        self.checkExpect(
            expect=1,
            actual=len(self.clause1))

    def test_len_2(self):
        self.checkExpect(
            expect=1,
            actual=len(self.clause2))

    def test_len_3(self):
        self.checkExpect(
            expect=2,
            actual=len(self.clause3))

    def test_len_4(self):
        self.checkExpect(
            expect=2,
            actual=len(self.clause4))

    def test_len_5(self):
        self.checkExpect(
            expect=2,
            actual=len(self.clause5))

    def test_len_6(self):
        self.checkExpect(
            expect=2,
            actual=len(self.clause6))
