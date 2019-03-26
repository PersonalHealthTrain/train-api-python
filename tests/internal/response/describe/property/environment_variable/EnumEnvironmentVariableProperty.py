from unittest.mock import patch
from pht.internal.response.describe.property.environment_variable import enum_by_name
from tests.base import BaseTest
from copy import copy, deepcopy


class EnumEnvironmentVariablePropertyTests(BaseTest):

    def setUp(self):
        self.enum1 = enum_by_name('FOO', ['VALUE1', 'VALUE2'])
        self.enum2 = enum_by_name('BAR', ['SINGLETON'])

    ###########################################################
    # Invalid arguments to EnumEnvironmentVariable
    ###########################################################
    # Invalid Name
    def test_invalid_enum_1(self):
        with self.assertRaises(TypeError):
            enum_by_name(True, ['SINGLETON'])

    def test_invalid_enum_2(self):
        with self.assertRaises(TypeError):
            enum_by_name({}, ['SINGLETON'])

    def test_invalid_enum_3(self):
        with self.assertRaises(TypeError):
            enum_by_name([], ['SINGLETON'])

    def test_invalid_enum_4(self):
        with self.assertRaises(ValueError):
            enum_by_name('akfgus', ['SINGLETON'])

    def test_invalid_enum_5(self):
        with self.assertRaises(ValueError):
            enum_by_name(None, ['SINGLETON'])

    # Invalid List of choices
    def test_invalid_enum_6(self):
        with self.assertRaises(TypeError):
            enum_by_name('FOO', True)

    def test_invalid_enum_7(self):
        with self.assertRaises(TypeError):
            enum_by_name('FOO', {})

    def test_invalid_enum_8(self):
        with self.assertRaises(ValueError):
            enum_by_name('FOO', [])

    def test_invalid_enum_9(self):
        with self.assertRaises(TypeError):
            enum_by_name('FOO', 'alfhu')

    def test_invalid_enum_10(self):
        with self.assertRaises(ValueError):
            enum_by_name('FOO', [])

    def test_invalid_enum_11(self):
        with self.assertRaises(TypeError):
            enum_by_name('FOO', 1)

    ###########################################################
    # Valid and invalid environment variable names
    ###########################################################

    def assert_invalid_env_name(self, name):
        self.assertValueError(lambda: enum_by_name(name, ["SINGLETON"]))

    def test_valid_environment_variable_1(self):
        enum_by_name('MY_URL', ["SINGLETON"])

    def test_valid_environment_variable_2(self):
        enum_by_name('A', ["SINGLETON"])

    def test_valid_environment_variable_3(self):
        enum_by_name('FOO', ["SINGLETON"])

    def test_valid_environment_variable_4(self):
        enum_by_name('TEST_THIS_URL', ["SINGLETON"])

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
    def test_equals_1(self):
        self.assertEqual(
            enum_by_name("FOO", ['SINGLETON']),
            enum_by_name("FOO", ['SINGLETON']))

    def test_equals_2(self):
        self.assertEqual(
            enum_by_name("BAR", ['SINGLETON']),
            enum_by_name("BAR", ['SINGLETON']))

    def test_equals_3(self):
        self.assertEqual(
            enum_by_name("BAZ", ['SINGLETON']),
            enum_by_name("BAZ", ['SINGLETON']))

    def test_equals_4(self):
        self.assertEqual(
            enum_by_name("MY_VARIABLE", ['SINGLETON']),
            enum_by_name("MY_VARIABLE", ['SINGLETON']))

    def test_equals_5(self):
        self.assertEqual(
            enum_by_name("SOME_OTHER_VARIABLE", ['SINGLETON']),
            enum_by_name("SOME_OTHER_VARIABLE", ['SINGLETON']))

    def test_unequal_env_by_name(self):
        self.assertUnequalCominationPairs([
            enum_by_name("FOO", ['SINGLETON']),
            enum_by_name("BAR", ['SINGLETON']),
            enum_by_name("MY_VARIABLE", ['SINGLETON']),
            enum_by_name("SOME_OTHER_VARIABLE", ['SINGLETON'])])

    def test_unequal_env_by_choices(self):
        self.assertUnequalCominationPairs([
            enum_by_name('FOO', ['SINGLETON']),
            enum_by_name('FOO', ['FOO', 'BAR']),
            enum_by_name('FOO', ['ARG1', 'ARG2'])])

    def test_unequal_env_by_name_and_choices(self):
        self.assertUnequalCominationPairs([
            enum_by_name('BLA', ['SINGLETON']), enum_by_name('BLUB', ['FOO', 'BAR']),
            enum_by_name('BLA', ['FOO', 'BAR']), enum_by_name('BLUB', ['ARG1', 'ARG2'])])

    ###########################################################
    # Hash
    ###########################################################

    def test_hash_1(self):
        self.assertIsEqual(2, len({self.enum1, self.enum2}))

    def test_hash_2(self):
        self.assertIsEqual(1, len({self.enum1, self.enum1}))

    def test_hash_3(self):
        self.assertIsEqual(
            enum_by_name('FOO', choices=['SINGLETON']),
            enum_by_name('FOO', choices=['SINGLETON']))

    ###########################################################
    # Check
    ###########################################################
    def test_check_true_1(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value'}):
            self.assertTrue(enum_by_name('FOO_BAR', ['value']).is_available())

    def test_check_true_2(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value1'}):
            self.assertTrue(enum_by_name('FOO_BAR', ['value1', 'value2']).is_available())

    def test_check_false_when_env_var_is_missing(self):
        with patch.dict('os.environ', {}):
            self.assertFalse(enum_by_name('FOO_BAR', ['value']).is_available())

    def test_check_false_when_value_is_not_allowed(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value1'}):
            self.assertFalse(enum_by_name('FOO_BAR', ['value2']).is_available())

    ###########################################################
    # __str__ and __repr__
    ###########################################################
    def test_str_1(self):
        self.assertEqual('Enum[name=FOO,choices=[\'VALUE1\', \'VALUE2\']]', str(self.enum1))

    def test_str_2(self):
        self.assertEqual('Enum[name=BAR,choices=[\'SINGLETON\']]', str(self.enum2))

    def test_repr_1(self):
        self.assertEqual('Enum[name=FOO,choices=[\'VALUE1\', \'VALUE2\']]', repr(self.enum1))

    def test_repr_2(self):
        self.assertEqual('Enum[name=BAR,choices=[\'SINGLETON\']]', repr(self.enum2))

    ###########################################################
    # Copy
    ###########################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.enum1)

    def test_copy_2(self):
        self.assertCopiesAreEqualOf(self.enum2)

    ###########################################################
    # get_value
    ###########################################################
    def test_get_value_1(self):    # TODO Test with fixed assertion method
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.assertEqual(self.enum1.get_value(), 'value1')

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAZ': 'value2'}):
            self.assertEqual(enum_by_name('BAZ', ['value2']).get_value(), 'value2')

    ###########################################################
    # type
    ###########################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['EnumEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
            actual=self.enum1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['EnumEnvironmentVariableProperty', 'EnvironmentVariableProperty', 'Property'],
            actual=self.enum2.type)

    ###########################################################
    # type_name
    ###########################################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='EnumEnvironmentVariableProperty',
            actual=self.enum1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='EnumEnvironmentVariableProperty',
            actual=self.enum2.type_name)

    ###########################################################
    # data
    ###########################################################
    def test_data_1(self):
        self.checkExpect(
            expect={
                "description": '',
                'environmentVariableName': 'FOO',
                'choices': ['VALUE1', 'VALUE2'],
                "state": {
                    "isAvailable": False,
                    "reason": "Environment variable 'FOO' not set"
                }
            },
            actual=self.enum1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={
                "description": '',
                'environmentVariableName': 'BAR',
                'choices': ['SINGLETON'],
                "state": {
                    "isAvailable": False,
                    "reason": "Environment variable 'BAR' not set"
                },
            },
            actual=self.enum2.data)

    ###########################################################
    # dict
    ###########################################################
    def test_simple_dict_1(self):
        self.checkExpect(
            expect={
                "description": '',
                'environmentVariableName': 'FOO',
                'choices': ['VALUE1', 'VALUE2'],
                "state": {
                    "isAvailable": False,
                    "reason": "Environment variable 'FOO' not set"
                },
                '@type': ['EnumEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'EnumEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.enum1.as_simple_dict())

    def test_simple_dict_2(self):
        self.checkExpect(
            expect={
                "description": '',
                'environmentVariableName': 'BAR',
                'choices': ['SINGLETON'],
                "state": {
                    "isAvailable": False,
                    "reason": "Environment variable 'BAR' not set"
                },
                '@type': ['EnumEnvironmentVariableProperty',
                          'EnvironmentVariableProperty',
                          'Property'],
                '@typeName': 'EnumEnvironmentVariableProperty',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.enum2.as_simple_dict())
