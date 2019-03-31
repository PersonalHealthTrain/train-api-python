from tests.base import BaseTest
from pht.internal.response.describe.formula.Clause import Clause
from pht.internal.response.describe.formula.CNF import ConjunctiveNormalForm


class CnfTests(BaseTest):

    def setUp(self):
        self.cnf1 = ConjunctiveNormalForm(Clause(3, 4), Clause(1, 2))
        self.cnf2 = ConjunctiveNormalForm(Clause(1))
        self.cnf3 = ConjunctiveNormalForm(Clause(1), Clause(1, 2))
        self.cnf4 = ConjunctiveNormalForm(Clause(-1, -2), Clause(-1, -2))

    ################################################################################
    # Empty CNF not allowed
    ################################################################################
    def test_empty_CNF_not_allowed(self):
        self.assertTypeError(lambda: ConjunctiveNormalForm())

    ################################################################################
    # Type Error
    ################################################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: ConjunctiveNormalForm(1))

    def test_type_error_2(self):
        self.assertTypeError(lambda: ConjunctiveNormalForm(False))

    def test_type_error_3(self):
        self.assertTypeError(lambda: ConjunctiveNormalForm({}))

    def test_type_error_4(self):
        self.assertTypeError(lambda: ConjunctiveNormalForm([]))

    def test_type_error_5(self):
        self.assertTypeError(lambda: ConjunctiveNormalForm('ad'))

    def test_type_error_6(self):
        self.assertTypeError(lambda: ConjunctiveNormalForm(None))

    ################################################################################
    # equals and hash
    ################################################################################
    def test_eq_1(self):
        self.assertIsEqual(ConjunctiveNormalForm(Clause(3, 4), Clause(1, 2)), self.cnf1)

    def test_eq_2(self):
        self.assertIsEqual(ConjunctiveNormalForm(Clause(1)), self.cnf2)

    def test_eq_3(self):
        self.assertIsEqual(ConjunctiveNormalForm(Clause(1), Clause(1, 2)), self.cnf3)

    def test_eq_4(self):
        self.assertIsEqual(ConjunctiveNormalForm(Clause(-1, -2), Clause(-1, -2)), self.cnf4)

    ################################################################################
    # Copy
    ################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.cnf1)

    def test_copy_2(self):
        self.assertCopiesAreEqualOf(self.cnf2)

    def test_copy_3(self):
        self.assertCopiesAreEqualOf(self.cnf3)

    def test_copy_4(self):
        self.assertCopiesAreEqualOf(self.cnf4)

    ################################################################################
    # as_dict
    ################################################################################
    def test_simple_dict_1(self):
        self.checkExpect(
            expect={
                'value': [[1, 2], [3, 4]],
                '@type': ['ConjunctiveNormalForm', 'Formula'],
                '@typeName': 'ConjunctiveNormalForm',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.cnf1.as_simple_mapping())

    def test_dict_2(self):
        self.checkExpect(
            expect={
                'value': [[1]],
                '@type': ['ConjunctiveNormalForm', 'Formula'],
                '@typeName': 'ConjunctiveNormalForm',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                }
            },
            actual=self.cnf2.as_simple_mapping())

    def test_dict_3(self):
        self.checkExpect(
            expect={
                'value': [[1], [1, 2]],
                '@type': ['ConjunctiveNormalForm', 'Formula'],
                '@typeName': 'ConjunctiveNormalForm',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.cnf3.as_simple_mapping())

    def test_dict_4(self):
        self.checkExpect(
            expect={
                'value': [[-2, -1]],
                '@type': ['ConjunctiveNormalForm', 'Formula'],
                '@typeName': 'ConjunctiveNormalForm',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.cnf4.as_simple_mapping())

    ################################################################################
    # type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['ConjunctiveNormalForm', 'Formula'],
            actual=self.cnf1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['ConjunctiveNormalForm', 'Formula'],
            actual=self.cnf2.type)

    def test_type_3(self):
        self.checkExpect(
            expect=['ConjunctiveNormalForm', 'Formula'],
            actual=self.cnf3.type)

    def test_type_4(self):
        self.checkExpect(
            expect=['ConjunctiveNormalForm', 'Formula'],
            actual=self.cnf4.type)

    ################################################################################
    # display
    ################################################################################
    def test_display_1(self):
        self.checkExpect(
            expect='ConjunctiveNormalForm',
            actual=self.cnf1.type_name)

    def test_display_2(self):
        self.checkExpect(
            expect='ConjunctiveNormalForm',
            actual=self.cnf2.type_name)

    def test_display_3(self):
        self.checkExpect(
            expect='ConjunctiveNormalForm',
            actual=self.cnf3.type_name)

    def test_display_4(self):
        self.checkExpect(
            expect='ConjunctiveNormalForm',
            actual=self.cnf4.type_name)

    ################################################################################
    # data
    ################################################################################
    def test_data_1(self):
        self.checkExpect(
            expect={'value': [[1, 2], [3, 4]]},
            actual=self.cnf1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'value': [[1]]},
            actual=self.cnf2.data)

    def test_data_3(self):
        self.checkExpect(
            expect={'value': [[1], [1, 2]]},
            actual=self.cnf3.data)

    def test_data_4(self):
        self.checkExpect(
            expect={'value': [[-2, -1]]},
            actual=self.cnf4.data)

    ################################################################################
    # str
    ################################################################################
    def test_str_1(self):
        self.checkExpect(
            expect='[[1, 2], [3, 4]]',
            actual=str(self.cnf1))

    def test_str_2(self):
        self.checkExpect(
            expect='[[1]]',
            actual=str(self.cnf2))

    def test_str_3(self):
        self.checkExpect(
            expect='[[1], [1, 2]]',
            actual=str(self.cnf3))

    def test_str_4(self):
        self.checkExpect(
            expect='[[-2, -1]]',
            actual=str(self.cnf4))

    ################################################################################
    # repr
    ################################################################################
    def test_repr_1(self):
        self.checkExpect(
            expect='[[1, 2], [3, 4]]',
            actual=repr(self.cnf1))

    def test_repr_2(self):
        self.checkExpect(
            expect='[[1]]',
            actual=repr(self.cnf2))

    def test_repr_3(self):
        self.checkExpect(
            expect='[[1], [1, 2]]',
            actual=repr(self.cnf3))

    def test_repr_4(self):
        self.checkExpect(
            expect='[[-2, -1]]',
            actual=repr(self.cnf4))

    ################################################################################
    # Contains
    ################################################################################
    def test_contains_1(self):
        self.assertMembership(
            for_container=self.cnf1,
            elements=[Clause(1, 2), Clause(3, 4)],
            not_elements=[Clause(1)])

    def test_contains_2(self):
        self.assertMembership(
            for_container=self.cnf2,
            elements=[Clause(1)],
            not_elements=[Clause(1, 2)])

    def test_contains_3(self):
        self.assertMembership(
            for_container=self.cnf3,
            elements=[Clause(1), Clause(1, 2)],
            not_elements=[Clause(-4, -2)])

    def test_contains_4(self):
        self.assertMembership(
            for_container=self.cnf4,
            elements=[Clause(-1, -2)],
            not_elements=[Clause(1)])

    ################################################################################
    # len
    ################################################################################
    def test_len_1(self):
        self.checkExpect(
            expect=2,
            actual=len(self.cnf1))

    def test_len_2(self):
        self.checkExpect(
            expect=1,
            actual=len(self.cnf2))

    def test_len_3(self):
        self.checkExpect(
            expect=2,
            actual=len(self.cnf3))

    def test_len_4(self):
        self.checkExpect(
            expect=1,
            actual=len(self.cnf4))

    ################################################################################
    # Value
    ################################################################################
    def test_value_1(self):
        self.checkExpect(
            expect=[[1, 2], [3, 4]],
            actual=self.cnf1.value)

    def test_value_2(self):
        self.checkExpect(
            expect=[[1]],
            actual=self.cnf2.value)

    def test_value_3(self):
        self.checkExpect(
            expect=[[1], [1, 2]],
            actual=self.cnf3.value)

    def test_value_4(self):
        self.checkExpect(
            expect=[[-2, -1]],
            actual=self.cnf4.value)
