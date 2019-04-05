from unittest.mock import patch
from pht.internal.response.describe.property.environment_variable import url_by_name
from tests.base import BaseTest


class UrlEnvironmentVariablePropertyTests(BaseTest):

    def setUp(self):
        self.url1 = url_by_name('FOO')
        self.url2 = url_by_name('BAR')
        self.url3 = url_by_name('MY_VARIABLE')
        self.url4 = url_by_name('SOME_OTHER_VARIABLE')

    def assert_invalid_env_name(self, name):
        with self.assertRaises(ValueError):
            url_by_name(name)

    ###########################################################
    # TypeError
    ###########################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: url_by_name(True))

    def test_type_error_2(self):
        self.assertTypeError(lambda: url_by_name({}))

    def test_type_error_3(self):
        self.assertTypeError(lambda: url_by_name([]))

    def test_type_error_4(self):
        self.assertTypeError(lambda: url_by_name(1))

    def test_type_error_5(self):
        self.assertTypeError(lambda: url_by_name(0.9661))

    ###########################################################
    # Value Error
    ###########################################################
    def test_valid_error_1(self):
        self.assertValueError(lambda: url_by_name('adaf'))

    def test_valid_error_2(self):
        self.assertTypeError(lambda: url_by_name(None))

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

    ###########################################################
    # Equals and not equals
    ###########################################################
    def test_eq_1(self):
        self.assertIsEqual(self.url1, url_by_name('FOO'))

    def test_eq_2(self):
        self.assertIsEqual(self.url2, url_by_name('BAR'))

    def test_eq_3(self):
        self.assertIsEqual(self.url3, url_by_name('MY_VARIABLE'))

    def test_eq_4(self):
        self.assertIsEqual(self.url4, url_by_name('SOME_OTHER_VARIABLE'))

    def test_unequal(self):
        self.assertUnequalCominationPairs([
            self.url1, self.url2, self.url3, self.url4])

    ###########################################################
    # Copy
    ###########################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.url1)

    def test_copy_2(self):
        self.assertCopiesAreEqualOf(self.url2)

    def test_copy_3(self):
        self.assertCopiesAreEqualOf(self.url3)

    def test_copy_4(self):
        self.assertCopiesAreEqualOf(self.url4)

    ###########################################################
    # dict
    ###########################################################
    def test_as_simple_dict_1(self):
        self.checkExpect(
            expect={
                'description': '',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'FOO\' not set'},
                '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                '@typeName': 'UrlEnvironmentVariableProperty',
                '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                }
            },
            actual=self.url1.as_simple_mapping())

    def test_as_simple_dict_2(self):
        self.checkExpect(
            expect={
                'description': '',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'BAR\' not set'},
                '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                '@typeName': 'UrlEnvironmentVariableProperty',
                '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                    }
            },
            actual=self.url2.as_simple_mapping())

    def test_as_simple_dict_3(self):
        self.checkExpect(
            expect={
                'description': '',
                'environmentVariableName': 'MY_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': "Environment variable 'MY_VARIABLE' not set"
                },
                '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                '@typeName': 'UrlEnvironmentVariableProperty',
                '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                    }
            },
            actual=self.url3.as_simple_mapping())

    def test_as_simple_dict_4(self):
        self.checkExpect(
            expect={
                'description': '',
                'environmentVariableName': 'SOME_OTHER_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': "Environment variable 'SOME_OTHER_VARIABLE' not set"},
                '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                '@typeName': 'UrlEnvironmentVariableProperty',
                '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                    }
            },
            actual=self.url4.as_simple_mapping())

    def test_as_simple_dict_5(self):
        with patch.dict('os.environ', {'FOO': 'value'}):
            self.checkExpect(
                expect={
                    'description': '',
                    'environmentVariableName': 'FOO',
                    'state': {
                        'isAvailable': True,
                        'reason': ''
                    },
                    '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                    '@typeName': 'UrlEnvironmentVariableProperty',
                    '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                    }
                },
                actual=self.url1.as_simple_mapping())

    @patch.dict('os.environ', {'BAR': 'value'})
    def test_as_simple_dict_6(self):
        self.checkExpect(
            expect={
                'description': '',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': True,
                    'reason': ''
                },
                '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                '@typeName': 'UrlEnvironmentVariableProperty',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                }
            },
            actual=self.url2.as_simple_mapping())

    @patch.dict('os.environ', {'MY_VARIABLE': 'value'})
    def test_as_simple_dict_7(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'MY_VARIABLE',
                'state': {
                    'isAvailable': True,
                    'reason': ''
                },
                '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                '@typeName': 'UrlEnvironmentVariableProperty',
                '@typeSystem': {
                    'name': 'pythonclass',
                    'version': '1.0'
                 }
            },
            actual=self.url3.as_simple_mapping())

    def test_as_simple_dict_8(self):
        with patch.dict('os.environ', {'SOME_OTHER_VARIABLE': 'value'}):
            self.checkMapping(
                expect={
                    'description': '',
                    'environmentVariableName': 'SOME_OTHER_VARIABLE',
                    'state': {
                        'isAvailable': True,
                        'reason': ''
                    },
                    '@type': ['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
                    '@typeName': 'UrlEnvironmentVariableProperty',
                    '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                    }
                },
                actual=self.url4.as_simple_mapping())

    ###########################################################
    # type
    ###########################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
            actual=self.url1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
            actual=self.url2.type)

    def test_type_3(self):
        self.checkExpect(
            expect=['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
            actual=self.url3.type)

    def test_type_4(self):
        self.checkExpect(
            expect=['UrlEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
            actual=self.url4.type)

    ###########################################################
    # type_name
    ###########################################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='UrlEnvironmentVariableProperty',
            actual=self.url1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='UrlEnvironmentVariableProperty',
            actual=self.url2.type_name)

    def test_type_name_3(self):
        self.checkExpect(
            expect='UrlEnvironmentVariableProperty',
            actual=self.url3.type_name)

    def test_type_name_4(self):
        self.checkExpect(
            expect='UrlEnvironmentVariableProperty',
            actual=self.url4.type_name)

    ###########################################################
    # data
    ###########################################################
    def test_data_1(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'FOO\' not set'
                }
            },
            actual=self.url1.data)

    def test_data_2(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'BAR\' not set'
                }
            },
            actual=self.url2.data)

    def test_data_3(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'MY_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'MY_VARIABLE\' not set'
                }
            },
            actual=self.url3.data)

    def test_data_4(self):
        self.checkExpect(
            expect={
                'description': '',
                'environmentVariableName': 'SOME_OTHER_VARIABLE',
                'state': {
                    'isAvailable': False,
                    'reason': 'Environment variable \'SOME_OTHER_VARIABLE\' not set'}},
            actual=self.url4.data)

    @patch.dict('os.environ', {'FOO': 'VALUE'})
    def test_data_5(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'FOO',
                'state': {
                    'isAvailable': True,
                    'reason': ''
                }
            },
            actual=self.url1.data)

    @patch.dict('os.environ', {'BAR': 'VALUE'})
    def test_data_6(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'BAR',
                'state': {
                    'isAvailable': True,
                    'reason': ''
                }
            },
            actual=self.url2.data)

    @patch.dict('os.environ', {'MY_VARIABLE': 'VALUE'})
    def test_data_7(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'MY_VARIABLE',
                'state': {
                    'isAvailable': True,
                    'reason': ''
                }
            },
            actual=self.url3.data)

    @patch.dict('os.environ', {'SOME_OTHER_VARIABLE': 'VALUE'})
    def test_data_8(self):
        self.checkMapping(
            expect={
                'description': '',
                'environmentVariableName': 'SOME_OTHER_VARIABLE',
                'state': {
                    'isAvailable': True,
                    'reason': ''
                }
            },
            actual=self.url4.data)

    ###########################################################
    # is available
    ###########################################################
    @patch.dict('os.environ', {'FOO': 'value'})
    def test_is_available_1_1(self):
        self.assertThat(self.url1.state().is_satisfied)

    @patch.dict('os.environ', {'FOO': ''})
    def test_is_available_1_2(self):
        self.assertThatNot(self.url1.state().is_satisfied)

    @patch.dict('os.environ', {'BAR': 'value'})
    def test_is_available_2_1(self):
        self.assertThat(self.url2.state().is_satisfied)

    def test_is_available_2_2(self):
        self.assertThatNot(self.url2.state().is_satisfied)

    @patch.dict('os.environ', {'MY_VARIABLE': 'value'})
    def test_is_available_3_1(self):
        self.assertThat(self.url3.state().is_satisfied)

    def test_is_available_3_2(self):
        self.assertThatNot(self.url3.state().is_satisfied)

    @patch.dict('os.environ', {'SOME_OTHER_VARIABLE': 'value'})
    def test_is_available_4_1(self):
        self.assertThat(self.url4.state().is_satisfied)

    def test_is_available_4_2(self):
        self.assertThatNot(self.url4.state().is_satisfied)

    ###########################################################
    # __str__
    ###########################################################
    def test_str_1(self):
        self.checkExpect(
            expect='Url[name=FOO]',
            actual=str(self.url1))

    def test_str_2(self):
        self.checkExpect(
            expect='Url[name=BAR]',
            actual=str(self.url2))

    def test_str_3(self):
        self.checkExpect(
            expect='Url[name=MY_VARIABLE]',
            actual=str(self.url3))

    def test_str_4(self):
        self.checkExpect(
            expect='Url[name=SOME_OTHER_VARIABLE]',
            actual=str(self.url4))

    ###########################################################
    # __repr__
    ###########################################################
    def test_repr_1(self):
        self.checkExpect(
            expect='Url[name=FOO]',
            actual=repr(self.url1))

    def test_repr_2(self):
        self.checkExpect(
            expect='Url[name=BAR]',
            actual=repr(self.url2))

    def test_repr_3(self):
        self.checkExpect(
            expect='Url[name=MY_VARIABLE]',
            actual=repr(self.url3))

    def test_repr_4(self):
        self.checkExpect(
            expect='Url[name=SOME_OTHER_VARIABLE]',
            actual=repr(self.url4))

    ###########################################################
    # get_value
    ###########################################################
    def test_get_value_1(self):
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.checkExpect(
                expect='value1',
                actual=self.url1.get_value())

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAR': ''}):
            self.checkExpect(
                expect='',
                actual=self.url2.get_value())

    def test_get_value_3(self):
        with self.assertRaises(KeyError):
            self.checkExpect(
                expect='',
                actual=self.url3.get_value())

    def test_get_value_4(self):
        with self.assertRaises(KeyError):
            self.checkExpect(
                expect='',
                actual=self.url4.get_value())
