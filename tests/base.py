import unittest
import copy


class BaseTest(unittest.TestCase):

    def checkExpect(self, expect, actual):
        self.assertEqual(expect, actual)

    def _assertError(self, func, error):
        with self.assertRaises(error):
            func()

    def assertValueError(self, func):
        self._assertError(func, ValueError)

    def assertTypeError(self, func):
        self._assertError(func, TypeError)

    def assertIsEqual(self, left, right):
        self.assertEqual(left, right)
        self.assertEqual(right, left)
        self.assertEqual(hash(left), hash(right))

    def assertCopiesAreEqual(self, item):
        c1 = item.copy()
        c2 = copy.copy(item)
        c3 = copy.deepcopy(item)
        self.assertIsEqual(c1, c2)
        self.assertIsEqual(c1, c3)
        self.assertIsEqual(c2, c3)
