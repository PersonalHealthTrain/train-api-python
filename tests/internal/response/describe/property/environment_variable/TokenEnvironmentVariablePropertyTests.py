from unittest.mock import patch
from pht.internal.response.describe.property.environment_variable import token_by_name
from tests.base import BaseTest


class TokenEnvironmentVariablePropertyTests(BaseTest):

    def setUp(self):
        self.token1 = token_by_name('FOO')
        self.token2 = token_by_name('BAR')
        self.token3 = token_by_name('MY_VARIABLE')
        self.token4 = token_by_name('SOME_OTHER_VARIABLE')

    def assert_invalid_env_name(self, name):
        with self.assertRaises(ValueError):
            token_by_name(name)

    ###########################################################
    # TypeError
    ###########################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: token_by_name(True))

    def test_type_error_2(self):
        self.assertTypeError(lambda: token_by_name({}))

    def test_type_error_3(self):
        self.assertTypeError(lambda: token_by_name([]))

    def test_type_error_4(self):
        self.assertTypeError(lambda: token_by_name(1))

    def test_type_error_5(self):
        self.assertTypeError(lambda: token_by_name(0.9661))

    ###########################################################
    # Value Error
    ###########################################################
    def test_valid_error_1(self):
        self.assertValueError(lambda: token_by_name('adaf'))

    def test_valid_error_2(self):
        self.assertValueError(lambda: token_by_name(None))

    def test_invalid_environment_variables_1(self):
        self.assert_invalid_env_name("")

    def test_invalid_environment_variables_2(self):
        self.assert_invalid_env_name("_")

    def test_invalid_environment_variables_3(self):
        self.assert_invalid_env_name(" ")

    def test_invalid_environment_variables_4(self):
        self.assert_invalid_env_name("AR_")

    def test_invalid_environment_variables_5(self):
        self.assert_invalid_env_name("sadsf")

    def test_invalid_environment_variables_6(self):
        self.assert_invalid_env_name("_HSGJD")

    def test_invalid_environment_variables_7(self):
        self.assert_invalid_env_name("HSG__JD")

    def test_invalid_environment_variables_8(self):
        self.assert_invalid_env_name(None)

    ###########################################################
    # Equals and not equals
    ###########################################################
    def test_eq_1(self):
        self.assertIsEqual(self.token1, token_by_name('FOO'))

    def test_eq_2(self):
        self.assertIsEqual(self.token2, token_by_name('BAR'))

    def test_eq_3(self):
        self.assertIsEqual(self.token3, token_by_name('MY_VARIABLE'))

    def test_eq_4(self):
        self.assertIsEqual(self.token4, token_by_name('SOME_OTHER_VARIABLE'))

    def test_unequal(self):
        self.assertNotEqual(self.token1, self.token2)
        self.assertNotEqual(self.token1, self.token3)
        self.assertNotEqual(self.token1, self.token4)
        self.assertNotEqual(self.token2, self.token3)
        self.assertNotEqual(self.token2, self.token4)
        self.assertNotEqual(self.token3, self.token4)

    ###########################################################
    # Copy
    ###########################################################
    def test_copy_1(self):
        self.assertCopiesAreEqual(self.token1)

    def test_copy_2(self):
        self.assertCopiesAreEqual(self.token2)

    def test_copy_3(self):
        self.assertCopiesAreEqual(self.token3)

    def test_copy_4(self):
        self.assertCopiesAreEqual(self.token4)

    ###########################################################
    # dict
    ###########################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'FOO\' not set'},
                'type': 'http://www.wikidata.org/entity/Q400857',
                'display': 'environmentVariable'
            }, actual=self.token1.as_dict()
        )

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'BAR\' not set'},
                'type': 'http://www.wikidata.org/entity/Q400857',
                'display': 'environmentVariable'}, actual=self.token2.as_dict()
        )

    def test_as_dict_3(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'MY_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': "Environment variable 'MY_VARIABLE' not set"
                },
                'type': 'http://www.wikidata.org/entity/Q400857',
                'display': 'environmentVariable'},
            actual=self.token3.as_dict())

    def test_as_dict_4(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'SOME_OTHER_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': "Environment variable 'SOME_OTHER_VARIABLE' not set"},
                'type': 'http://www.wikidata.org/entity/Q400857',
                'display': 'environmentVariable'
            },
            actual=self.token4.as_dict())

    def test_as_dict_5(self):
        with patch.dict('os.environ', {'FOO': 'value'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'FOO',
                    'state': {
                        'isAvailable': True,
                        'reason': None
                    },
                    'type': 'http://www.wikidata.org/entity/Q400857',
                    'display': 'environmentVariable'
                },
                actual=self.token1.as_dict())

    def test_as_dict_6(self):
        with patch.dict('os.environ', {'BAR': 'value'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'BAR',
                    'state': {
                        'isAvailable': True,
                        'reason': None
                    },
                    'type': 'http://www.wikidata.org/entity/Q400857',
                    'display': 'environmentVariable'
                },
                actual=self.token2.as_dict())

    def test_as_dict_7(self):
        with patch.dict('os.environ', {'MY_VARIABLE': 'value'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'MY_VARIABLE',
                    'state': {
                        'isAvailable': True,
                        'reason': None
                    },
                    'type': 'http://www.wikidata.org/entity/Q400857',
                    'display': 'environmentVariable'
                },
                actual=self.token3.as_dict())

    def test_as_dict_8(self):
        with patch.dict('os.environ', {'SOME_OTHER_VARIABLE': 'value'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'SOME_OTHER_VARIABLE',
                    'state': {
                        'isAvailable': True,
                        'reason': None
                    },
                    'type': 'http://www.wikidata.org/entity/Q400857',
                    'display': 'environmentVariable'
                },
                actual=self.token4.as_dict())

    ###########################################################
    # type
    ###########################################################
    def test_type_1(self):
        self.checkExpect(
            expect='http://www.wikidata.org/entity/Q400857',
            actual=self.token1.type)

    def test_type_2(self):
        self.checkExpect(
            expect='http://www.wikidata.org/entity/Q400857',
            actual=self.token2.type)

    def test_type_3(self):
        self.checkExpect(
            expect='http://www.wikidata.org/entity/Q400857',
            actual=self.token3.type)

    def test_type_4(self):
        self.checkExpect(
            expect='http://www.wikidata.org/entity/Q400857',
            actual=self.token4.type)

    ###########################################################
    # display
    ###########################################################
    def test_display_1(self):
        self.checkExpect(
            expect='environmentVariable',
            actual=self.token1.display)

    def test_display_2(self):
        self.checkExpect(
            expect='environmentVariable',
            actual=self.token2.display)

    def test_display_3(self):
        self.checkExpect(
            expect='environmentVariable',
            actual=self.token3.display)

    def test_display_4(self):
        self.checkExpect(
            expect='environmentVariable',
            actual=self.token4.display)

    ###########################################################
    # data
    ###########################################################
    def test_data_1(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'FOO\' not set'}},
            actual=self.token1.data
        )

    def test_data_2(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'BAR\' not set'}},
            actual=self.token2.data)

    def test_data_3(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'MY_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'MY_VARIABLE\' not set'}},
            actual=self.token3.data)

    def test_data_4(self):
        self.checkExpect(
            expect={
                'description': None,
                'target': 'token',
                'name': 'SOME_OTHER_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'SOME_OTHER_VARIABLE\' not set'}},
            actual=self.token4.data)

    def test_data_5(self):
        with patch.dict('os.environ', {'FOO': 'VALUE'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'FOO',
                    'state': {
                        'isAvailable': True,
                        'reason': None}},
                actual=self.token1.data)

    def test_data_6(self):
        with patch.dict('os.environ', {'BAR': 'VALUE'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'BAR',
                    'state': {
                        'isAvailable': True,
                        'reason': None}},
                actual=self.token2.data)

    def test_data_7(self):
        with patch.dict('os.environ', {'MY_VARIABLE': 'VALUE'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'MY_VARIABLE',
                    'state': {
                        'isAvailable': True,
                        'reason': None}},
                actual=self.token3.data)

    def test_data_8(self):
        with patch.dict('os.environ', {'SOME_OTHER_VARIABLE': 'VALUE'}):
            self.checkExpect(
                expect={
                    'description': None,
                    'target': 'token',
                    'name': 'SOME_OTHER_VARIABLE',
                    'state': {
                        'isAvailable': True,
                        'reason': None}},
                actual=self.token4.data)

    ###########################################################
    # is available
    ###########################################################
    def test_is_available_1(self):
        with patch.dict('os.environ', {'FOO': 'value'}):
            self.assertTrue(self.token1.is_available())
        self.assertFalse(self.token1.is_available())

    def test_is_available_2(self):
        with patch.dict('os.environ', {'BAR': 'value'}):
            self.assertTrue(self.token2.is_available())
        self.assertFalse(self.token2.is_available())

    def test_is_available_3(self):
        with patch.dict('os.environ', {'MY_VARIABLE': 'value'}):
            self.assertTrue(self.token3.is_available())
        self.assertFalse(self.token3.is_available())

    def test_is_available_4(self):
        with patch.dict('os.environ', {'SOME_OTHER_VARIABLE': 'value'}):
            self.assertTrue(self.token4.is_available())
        self.assertFalse(self.token4.is_available())

    ###########################################################
    # __str__
    ###########################################################
    def test_str_1(self):
        self.checkExpect(
            expect='Token[name=FOO]',
            actual=str(self.token1))

    def test_str_2(self):
        self.checkExpect(
            expect='Token[name=BAR]',
            actual=str(self.token2))

    def test_str_3(self):
        self.checkExpect(
            expect='Token[name=MY_VARIABLE]',
            actual=str(self.token3))

    def test_str_4(self):
        self.checkExpect(
            expect='Token[name=SOME_OTHER_VARIABLE]',
            actual=str(self.token4))

    ###########################################################
    # __repr__
    ###########################################################
    def test_repr_1(self):
        self.checkExpect(
            expect='Token[name=FOO]',
            actual=repr(self.token1))

    def test_repr_2(self):
        self.checkExpect(
            expect='Token[name=BAR]',
            actual=repr(self.token2))

    def test_repr_3(self):
        self.checkExpect(
            expect='Token[name=MY_VARIABLE]',
            actual=repr(self.token3))

    def test_repr_4(self):
        self.checkExpect(
            expect='Token[name=SOME_OTHER_VARIABLE]',
            actual=repr(self.token4))

    ###########################################################
    # get_value
    ###########################################################
    def test_get_value_1(self):
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.checkExpect(
                expect='value1',
                actual=self.token1.get_value())

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAR': ''}):
            self.checkExpect(
                expect='',
                actual=self.token2.get_value())

    def test_get_value_3(self):
        with self.assertRaises(KeyError):
            self.checkExpect(
                expect='',
                actual=self.token3.get_value())

    def test_get_value_4(self):
        with self.assertRaises(KeyError):
            self.checkExpect(
                expect='',
                actual=self.token4.get_value())

    ###########################################################
    # target
    ###########################################################
    def test_target_1(self):
        self.checkExpect(
            expect='token',
            actual=self.token1.target)

    def test_target_2(self):
        self.checkExpect(
            expect='token',
            actual=self.token2.target)

    def test_target_3(self):
        self.checkExpect(
            expect='token',
            actual=self.token3.target)

    def test_target_4(self):
        self.checkExpect(
            expect='token',
            actual=self.token4.target)