import unittest
from pht.internal.describe.property import url_by_name
from pht.train.requirement import Require, Any


class CnfBuilder2Tests(unittest.TestCase):
    """
    Tests for Require and Forbid, now Any
    """

    def setUp(self):
        self.prop1 = url_by_name('FOO')
        self.prop2 = url_by_name('BAR')
        self.prop3 = url_by_name('BAZ')

    # 0 0 1
    def test_builder_1(self):
        c = Require(self.prop1) & Any(Require(self.prop2) | Require(self.prop3))
        self.assertEqual('[[1], [2, 3]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('FOO'), 2: url_by_name('BAR'), 3: url_by_name('BAZ')}, c.props)

    def test_builder_2(self):
        c = Any(Require(self.prop1) | Require(self.prop2) | Require(self.prop3))
        self.assertEqual('[[1, 2, 3]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('FOO'), 2: url_by_name('BAR'), 3: url_by_name('BAZ')}, c.props)
