import unittest


class BaseTest(unittest.TestCase):

    def checkExpect(self, expect, actual):
        self.assertEqual(expect, actual)
