from tests.base import BaseTest
from pht.internal.util.typetest import is_primitive, is_list


class TypetestTests(BaseTest):

    def test_is_primitive_1(self):
        self.assertTrue(is_primitive(1))

    def test_is_primitive_2(self):
        self.assertTrue(is_primitive(True))

    def test_is_primitive_3(self):
        self.assertTrue(is_primitive(False))

    def test_is_primitive_4(self):
        self.assertTrue(is_primitive(0))

    def test_is_primitive_5(self):
        self.assertTrue(is_primitive(0.0))

    def test_is_primitive_6(self):
        self.assertTrue(is_primitive(''))

    def test_is_primitive_7(self):
        self.assertTrue(is_primitive(None))

    def test_is_primitive_8(self):
        self.assertTrue(is_primitive('foo'))

    def test_is_primitive_9(self):
        self.assertTrue(is_primitive(42))

    def test_is_primitive_10(self):
        self.assertTrue(is_primitive(-42))

    def test_is_primitive_11(self):
        self.assertTrue(is_primitive(42.42))

    def test_is_primitive_12(self):
        self.assertTrue(is_primitive(-13.12))

    def test_is_not_primitive_1(self):
        self.assertFalse(is_primitive([]))

    def test_is_not_primitive_2(self):
        self.assertFalse(is_primitive({}))

    def test_is_not_primitive_3(self):
        self.assertFalse(is_primitive(range(6)))

    def test_is_list_1(self):
        self.assertTrue(is_list([]))

    def test_is_list_2(self):
        self.assertTrue([1, 2])

    def test_is_list_3(self):
        self.assertTrue([1])

    def test_is_list_4(self):
        self.assertTrue(list(range(3)))

    def test_is_not_list_1(self):
        self.assertFalse(is_list(range(3)))

