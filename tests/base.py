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

        self.assertIsEqual(item, c1)
        self.assertIsEqual(item, c2)
        self.assertIsEqual(item, c3)

        # Assert that copy rely creates a new instance and not references the original
        self.assertIsNot(c1, item)
        self.assertIsNot(c2, item)
        self.assertIsNot(c3, item)
