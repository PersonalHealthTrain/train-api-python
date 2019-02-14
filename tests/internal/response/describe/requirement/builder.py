import unittest
from pht.internal.response.describe.requirement import Forbid, Require, Any
from pht.internal.response.describe.property.environment_variable import url_by_name


class CnfBuilder1Tests(unittest.TestCase):
    """
    Tests for Require and Forbid, now Any
    """

    def setUp(self):
        self.prop1 = url_by_name('FOO')
        self.prop2 = url_by_name('BAR')
        self.prop3 = url_by_name('BAZ')

    # 0 0 1
    def test_builder_1(self):
        c = Require(self.prop1)
        self.assertEqual('[[1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('FOO')}, c.props)

    # 0 0 2
    def test_builder_2(self):
        c = Forbid(self.prop1)
        self.assertEqual('[[-1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('FOO')}, c.props)

    # 0 1 0
    def test_builder_3(self):
        c = Require(self.prop2)
        self.assertEqual('[[1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAR')}, c.props)

    # 0 1 1
    def test_builder_4(self):
        c = Require(self.prop2) & Require(self.prop1)
        self.assertEqual('[[1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAR'), 2: url_by_name('FOO')}, c.props)

    # 0 1 2
    def test_builder_5(self):
        c = Require(self.prop2) & Forbid(self.prop1)
        self.assertEqual('[[-2], [1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAR'), 2: url_by_name('FOO')}, c.props)

    # 0 2 0
    def test_builder_6(self):
        c = Forbid(self.prop2)
        self.assertEqual('[[-1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAR')}, c.props)

    # 0 2 1
    def test_builder_7(self):
        c = Forbid(self.prop2) & Require(self.prop1)
        self.assertEqual('[[-1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAR'), 2: url_by_name('FOO')}, c.props)

    # 0 2 2
    def test_builder_8(self):
        c = Forbid(self.prop2) & Forbid(self.prop1)
        self.assertEqual('[[-2], [-1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAR'), 2: url_by_name('FOO')}, c.props)

    # 1 0 0
    def test_builder_10(self):
        c = Require(self.prop3)
        self.assertEqual('[[1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ')}, c.props)

    # 1 0 1
    def test_builder_11(self):
        c = Require(self.prop3) & Require(self.prop1)
        self.assertEqual('[[1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('FOO')}, c.props)

    # 1 0 2
    def test_builder_12(self):
        c = Require(self.prop3) & Forbid(self.prop1)
        self.assertEqual('[[-2], [1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('FOO')}, c.props)

    # 1 1 0
    def test_builder_13(self):
        c = Require(self.prop3) & Require(self.prop2)
        self.assertEqual('[[1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR')}, c.props)

    # 1 1 1
    def test_builder_14(self):
        c = Require(self.prop3) & Require(self.prop2) & Require(self.prop1)
        self.assertEqual('[[1], [2], [3]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)

    # 1 1 2
    def test_builder_15(self):
        c = Require(self.prop3) & Require(self.prop2) & Forbid(self.prop1)
        self.assertEqual('[[-3], [1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)

    # 1 2 0
    def test_builder_16(self):
        c = Require(self.prop3) & Forbid(self.prop2)
        self.assertEqual('[[-2], [1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR')}, c.props)

    # 1 2 1
    def test_builder_17(self):
        c = Require(self.prop3) & Forbid(self.prop2) & Require(self.prop1)
        self.assertEqual('[[-2], [1], [3]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)

    # 1 2 2
    def test_builder_18(self):
        c = Require(self.prop3) & Forbid(self.prop2) & Forbid(self.prop1)
        self.assertEqual('[[-3], [-2], [1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)

    # 2 0 0
    def test_builder_19(self):
        c = Forbid(self.prop3)
        self.assertEqual('[[-1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ')}, c.props)

    # 2 0 1
    def test_builder_20(self):
        c = Forbid(self.prop3) & Require(self.prop1)
        self.assertEqual('[[-1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('FOO')}, c.props)

    # 2 0 2
    def test_builder_21(self):
        c = Forbid(self.prop3) & Forbid(self.prop1)
        self.assertEqual('[[-2], [-1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('FOO')}, c.props)

    # 2 1 0
    def test_builder_22(self):
        c = Forbid(self.prop3) & Require(self.prop2)
        self.assertEqual('[[-1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR')}, c.props)

    # 2 1 1
    def test_builder_23(self):
        c = Forbid(self.prop3) & Require(self.prop2) & Require(self.prop1)
        self.assertEqual('[[-1], [2], [3]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)

    # 2 1 2
    def test_builder_24(self):
        c = Forbid(self.prop3) & Require(self.prop2) & Forbid(self.prop1)
        self.assertEqual('[[-3], [-1], [2]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)

    # 2 2 0
    def test_builder_25(self):
        c = Forbid(self.prop3) & Forbid(self.prop2)
        self.assertEqual('[[-2], [-1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR')}, c.props)

    # 2 2 1
    def test_builder_26(self):
        c = Forbid(self.prop3) & Forbid(self.prop2) & Require(self.prop1)
        self.assertEqual('[[-2], [-1], [3]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)

    # 2 2 2
    def test_builder_27(self):
        c = Forbid(self.prop3) & Forbid(self.prop2) & Forbid(self.prop1)
        self.assertEqual('[[-3], [-2], [-1]]', str(c.cnf()))
        self.assertDictEqual({1: url_by_name('BAZ'), 2: url_by_name('BAR'), 3: url_by_name('FOO')}, c.props)


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
