from tests.base import BaseTest
from pht.internal.util.require import type_is_int, type_is_str, type_is_str_or_none, type_is_not_none
from pht.internal.util.predicate import is_not_none, is_positive


class RequireTests(BaseTest):

    ######################################################
    # type_is_int
    ######################################################
    def test_type_is_int_1(self):
        self.assertTypeError(lambda: type_is_int('foo'))

    def test_type_is_int_2(self):
        self.assertTypeError(lambda: type_is_int({}))

    def test_type_is_int_3(self):
        self.assertTypeError(lambda: type_is_int(1.5))

    def test_type_is_int_4(self):
        self.assertTypeError(lambda: type_is_int(True))

    def test_type_is_int_5(self):
        self.assertTypeError(lambda: type_is_int(False))

    def test_type_is_int_6(self):
        self.assertTypeError(lambda: type_is_int(None))

    def test_type_is_int_7(self):
        self.assertTypeError(lambda: type_is_int([]))

    ######################################################
    # type_is_str
    ######################################################
    def test_type_is_str_1(self):
        self.assertTypeError(lambda: type_is_str(1))

    def test_type_is_str_2(self):
        self.assertTypeError(lambda: type_is_str(True))

    def test_type_is_str_3(self):
        self.assertTypeError(lambda: type_is_str(False))

    def test_type_is_str_4(self):
        self.assertTypeError(lambda: type_is_str(None))

    def test_type_is_str_5(self):
        self.assertTypeError(lambda: type_is_str(0.987))

    def test_type_is_str_6(self):
        self.assertNotRaises(lambda: type_is_str('foo'))

    ######################################################
    # type_is_str or None
    ######################################################
    def test_type_is_str_or_none_1(self):
        self.assertTypeError(lambda: type_is_str_or_none(1))

    def test_type_is_str_or_none_2(self):
        self.assertTypeError(lambda: type_is_str_or_none(True))

    def test_type_is_str_or_none_3(self):
        self.assertTypeError(lambda: type_is_str_or_none(False))

    def test_type_is_str_or_none_4(self):
        self.assertTypeError(lambda: type_is_str_or_none(0.987))

    def test_type_is_str_or_none_5(self):
        self.assertNotRaises(lambda: type_is_str_or_none('foo'))

    def test_type_is_str_or_none_6(self):
        self.assertNotRaises(lambda: type_is_str_or_none(None))

    ######################################################
    # is_not_none
    ######################################################
    def test_is_not_none_1(self):
        self.assertTrue(is_not_none(True))

    def test_is_not_none_2(self):
        self.assertTrue(is_not_none(False))

    def test_is_not_none_3(self):
        self.assertTrue(is_not_none(''))

    def test_is_not_none_4(self):
        self.assertTrue(is_not_none(623))

    def test_is_not_none_5(self):
        self.assertTrue(is_not_none(7.1))

    def test_is_not_none_6(self):
        self.assertFalse(is_not_none(None))

    ######################################################
    # is_positive
    ######################################################
    def test_is_positive_1(self):
        self.assertTrue(is_positive(1))

    def test_is_positive_2(self):
        self.assertTrue(is_positive(100))

    def test_is_negative_3(self):
        self.assertFalse(is_positive(0))

    def test_is_negative_4(self):
        self.assertFalse(is_positive(-1))

    def test_is_negative_5(self):
        self.assertFalse(is_positive(-42))

    ######################################################
    # type_is_not_none
    ######################################################
    def test_type_is_not_none_1(self):
        self.assertNotRaises(lambda: type_is_not_none('foo'))

    def test_type_is_not_none_2(self):
        self.assertNotRaises(lambda: type_is_not_none(1))

    def test_type_is_not_none_3(self):
        self.assertTypeError(lambda: type_is_not_none(None))
