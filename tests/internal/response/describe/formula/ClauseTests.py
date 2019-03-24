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
        self.assertMembership(
            for_container=self.clause1,
            elements=[1],
            not_elements=[2])

    def test_iter_2(self):
        self.assertMembership(
            for_container=self.clause2,
            elements=[-1],
            not_elements=[1])

    def test_iter_3(self):
        self.assertMembership(
            for_container=self.clause3,
            elements=[1, 2],
            not_elements=[-1, -2, 0, 117])

    def test_iter_4(self):
        self.assertMembership(
            for_container=self.clause4,
            elements=[-1, 2],
            not_elements=[1, -2, -0, -5])

    def test_iter_5(self):
        self.assertMembership(
            for_container=self.clause5,
            elements=[1, -2],
            not_elements=[-1, 2, 0, -17])

    def test_iter_6(self):
        self.assertMembership(
            for_container=self.clause6,
            elements=[-1, -2],
            not_elements=[1, 2, 0, 255])

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
        self.assertMembership(
            for_container=self.clause1,
            elements=[1])

    def test_contains_2(self):
        self.assertMembership(
            for_container=self.clause2,
            not_elements=[1])

    def test_contains_3(self):
        self.assertMembership(
            for_container=self.clause3,
            elements=[1, 2],
            not_elements=[-1, -2])

    def test_contains_4(self):
        self.assertMembership(
            for_container=self.clause4,
            elements=[-1, 2],
            not_elements=[1, -2])

    def test_contains_5(self):
        self.assertMembership(
            for_container=self.clause5,
            elements=[-2, 1],
            not_elements=[-1, 2])

    def test_contains_6(self):
        self.assertMembership(
            for_container=self.clause6,
            elements=[-1, -2],
            not_elements=[1, 2])

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
