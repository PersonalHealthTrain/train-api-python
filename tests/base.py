import unittest
import copy
from itertools import combinations
from pht.internal.util.typetest import is_hashable


class BaseTest(unittest.TestCase):

    def checkExpect(self, expect, actual):
        self.assertEqual(expect, actual)

    def _assertError(self, func, error):
        with self.assertRaises(error):
            func()

    def assertThat(self, test):
        self.assertTrue(test)

    def assertThatNot(self, test):
        self.assertFalse(test)

    def assertValueError(self, func):
        self._assertError(func, ValueError)

    def assertTypeError(self, func):
        self._assertError(func, TypeError)

    def assertUnequalCominationPairs(self, items):
        for pair in combinations(items, 2):
            self.assertNotEqual(pair[0], pair[1])

    def assertMembership(self, *, for_container, elements=None, not_elements=None):
        if elements is None:
            elements = []
        if not_elements is None:
            not_elements = []
        for element in elements:
            self.assertIn(element, for_container)
        for element in not_elements:
            self.assertNotIn(element, for_container)

    def assertIsEqual(self, left, right):
        self.assertEqual(left, right)
        self.assertEqual(right, left)

        # If the types are Hashable, the hash values need to be the same
        if is_hashable(left) and is_hashable(right):
            self.assertEqual(hash(left), hash(right))

    def assertCopiesAreEqualOf(self, item):
        c1 = item.deepcopy()
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
