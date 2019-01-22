import unittest
from copy import copy, deepcopy
from pht.internal import CNF, Clause


class CnfTests(unittest.TestCase):

    def setUp(self):
        self.cnf1 = CNF(Clause(3, 4), Clause(1, 2))
        self.cnf2 = CNF(Clause(1))
        self.cnf3 = CNF(Clause(1), Clause(1, 2))
        self.cnf4 = CNF(Clause(-1, -2), Clause(-1, -2))

    ################################################################################
    # str
    ################################################################################
    def test_str_1(self):
        self.assertEqual('[[1, 2], [3, 4]]', str(self.cnf1))

    def test_str_2(self):
        self.assertEqual('[[1]]', str(self.cnf2))

    def test_str_3(self):
        self.assertEqual('[[1], [1, 2]]', str(self.cnf3))

    def test_str_4(self):
        self.assertEqual('[[-2, -1]]', str(self.cnf4))

    ################################################################################
    # repr
    ################################################################################
    def test_repr_1(self):
        self.assertEqual('[[1, 2], [3, 4]]', repr(self.cnf1))

    def test_repr_2(self):
        self.assertEqual('[[1]]', repr(self.cnf2))

    def test_repr_3(self):
        self.assertEqual('[[1], [1, 2]]', repr(self.cnf3))

    def test_repr_4(self):
        self.assertEqual('[[-2, -1]]', repr(self.cnf4))

    ################################################################################
    # dict
    ################################################################################
    def test_dict_1(self):
        expect = {'value': [[1, 2], [3, 4]], 'type': 'https://www.wikidata.org/wiki/Q846564', 'display': 'ConjunctiveNormalForm'}
        actual = self.cnf1.dict()
        self.assertDictEqual(expect, actual)

    def test_dict_2(self):
        expect = {'value': [[1]], 'type': 'https://www.wikidata.org/wiki/Q846564', 'display': 'ConjunctiveNormalForm'}
        actual = self.cnf2.dict()
        self.assertDictEqual(expect, actual)

    def test_dict_3(self):
        expect = {'value': [[1], [1, 2]], 'type': 'https://www.wikidata.org/wiki/Q846564', 'display': 'ConjunctiveNormalForm'}
        actual = self.cnf3.dict()
        self.assertDictEqual(expect, actual)

    def test_dict_4(self):
        expect = {'value': [[-2, -1]], 'type': 'https://www.wikidata.org/wiki/Q846564', 'display': 'ConjunctiveNormalForm'}
        actual = self.cnf4.dict()
        self.assertDictEqual(expect, actual)

    ################################################################################
    # data
    ################################################################################
    def test_data_1(self):
        expect = {'value': [[1, 2], [3, 4]]}
        actual = self.cnf1.data
        self.assertDictEqual(expect, actual)

    def test_data_2(self):
        expect = {'value': [[1]]}
        actual = self.cnf2.data
        self.assertDictEqual(expect, actual)

    def test_data_3(self):
        expect = {'value': [[1], [1, 2]]}
        actual = self.cnf3.data
        self.assertDictEqual(expect, actual)

    def test_data_4(self):
        expect = {'value': [[-2, -1]]}
        actual = self.cnf4.data
        self.assertDictEqual(expect, actual)

    ################################################################################
    # display
    ################################################################################
    def test_display_1(self):
        expect = 'ConjunctiveNormalForm'
        actual = self.cnf1.display
        self.assertEqual(expect, actual)

    def test_display_2(self):
        expect = 'ConjunctiveNormalForm'
        actual = self.cnf2.display
        self.assertEqual(expect, actual)

    def test_display_3(self):
        expect = 'ConjunctiveNormalForm'
        actual = self.cnf3.display
        self.assertEqual(expect, actual)

    def test_display_4(self):
        expect = 'ConjunctiveNormalForm'
        actual = self.cnf4.display
        self.assertEqual(expect, actual)

    ################################################################################
    # type
    ################################################################################
    def test_type_1(self):
        expect = 'https://www.wikidata.org/wiki/Q846564'
        actual = self.cnf1.type
        self.assertEqual(expect, actual)

    def test_type_2(self):
        expect = 'https://www.wikidata.org/wiki/Q846564'
        actual = self.cnf2.type
        self.assertEqual(expect, actual)

    def test_type_3(self):
        expect = 'https://www.wikidata.org/wiki/Q846564'
        actual = self.cnf3.type
        self.assertEqual(expect, actual)

    def test_type_4(self):
        expect = 'https://www.wikidata.org/wiki/Q846564'
        actual = self.cnf4.type
        self.assertEqual(expect, actual)

    ################################################################################
    # Empty CNF not allowed
    ################################################################################
    def test_empty_CNF_not_allowed(self):
        with self.assertRaises(TypeError):
            CNF()

    ################################################################################
    # Value
    ################################################################################
    def test_value_1(self):
        expect = [[1, 2], [3, 4]]
        actual = self.cnf1.value()
        self.assertListEqual(expect, actual)

    def test_value_2(self):
        expect = [[1]]
        actual = self.cnf2.value()
        self.assertListEqual(expect, actual)

    def test_value_3(self):
        expect = [[1], [1, 2]]
        actual = self.cnf3.value()
        self.assertListEqual(expect, actual)

    def test_value_4(self):
        expect = [[-2, -1]]
        actual = self.cnf4.value()
        self.assertListEqual(expect, actual)

    ################################################################################
    # Contains
    ################################################################################
    def test_contains_1(self):
        self.assertIn(Clause(1, 2), self.cnf1)
        self.assertIn(Clause(3, 4), self.cnf1)
        self.assertNotIn(Clause(1), self.cnf1)

    def test_contains_2(self):
        self.assertIn(Clause(1), self.cnf2)
        self.assertNotIn(Clause(1, 2), self.cnf2)

    def test_contains_3(self):
        self.assertIn(Clause(1), self.cnf3)
        self.assertIn(Clause(1, 2), self.cnf3)
        self.assertNotIn(Clause(-4, -2), self.cnf3)

    def test_contains_4(self):
        self.assertIn(Clause(-1, -2), self.cnf4)
        self.assertNotIn(Clause(1), self.cnf4)

    ################################################################################
    # equals and hash
    ################################################################################
    def test_eq_1(self):
        cnf = CNF(Clause(2, 1), Clause(3, 4))
        self.assertEqual(cnf, self.cnf1)
        self.assertEqual(hash(cnf), hash(self.cnf1))

    def test_eq_2(self):
        cnf = CNF(Clause(1))
        self.assertEqual(cnf, self.cnf2)
        self.assertEqual(hash(cnf), hash(self.cnf2))

    def test_eq_3(self):
        cnf = CNF(Clause(1), Clause(1, 2))
        self.assertEqual(cnf, self.cnf3)
        self.assertEqual(hash(cnf), hash(self.cnf3))

    def test_eq_4(self):
        cnf = CNF(Clause(-1, -2), Clause(-1, -2))
        self.assertEqual(cnf, self.cnf4)
        self.assertEqual(hash(cnf), hash(self.cnf4))

    ################################################################################
    # len
    ################################################################################
    def test_len_1(self):
        expect = 2
        actual = len(self.cnf1)
        self.assertEqual(expect, actual)

    def test_len_2(self):
        expect = 1
        actual = len(self.cnf2)
        self.assertEqual(expect, actual)

    def test_len_3(self):
        expect = 2
        actual = len(self.cnf3)
        self.assertEqual(expect, actual)

    def test_len_4(self):
        expect = 1
        actual = len(self.cnf4)
        self.assertEqual(expect, actual)

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        self.assertEqual(self.cnf1.copy(), self.cnf1)
        self.assertEqual(copy(self.cnf1), self.cnf1)
        self.assertEqual(deepcopy(self.cnf1), self.cnf1)

    def test_copy_2(self):
        self.assertEqual(self.cnf2.copy(), self.cnf2)
        self.assertEqual(copy(self.cnf2), self.cnf2)
        self.assertEqual(deepcopy(self.cnf2), self.cnf2)

    def test_copy_3(self):
        self.assertEqual(self.cnf3.copy(), self.cnf3)
        self.assertEqual(copy(self.cnf3), self.cnf3)
        self.assertEqual(deepcopy(self.cnf3), self.cnf3)

    def test_copy_4(self):
        self.assertEqual(self.cnf4.copy(), self.cnf4)
        self.assertEqual(copy(self.cnf4), self.cnf4)
        self.assertEqual(deepcopy(self.cnf4), self.cnf4)
