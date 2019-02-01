import unittest
from unittest.mock import patch
from copy import copy, deepcopy
from pht.requirement.env import url_by_name, token_by_name, enum_by_name


class UrlEnvironmentVariablePropertyTests(unittest.TestCase):

    def setUp(self):
        self.url1 = url_by_name('FOO')
        self.url2 = url_by_name('BAR')

    ###########################################################
    # Invalid arguments to URLEnvironmentVariable
    ###########################################################
    def test_invalid_url_1(self):
        with self.assertRaises(TypeError):
            url_by_name(True)

    def test_invalid_url_2(self):
        with self.assertRaises(TypeError):
            url_by_name({})

    def test_invalid_url_3(self):
        with self.assertRaises(TypeError):
            url_by_name([])

    def test_invalid_url_4(self):
        with self.assertRaises(ValueError):
            url_by_name('ldj')

    def test_invalid_url_5(self):
        with self.assertRaises(ValueError):
            url_by_name(None)

    ###########################################################
    # Valid and invalid environment variable names
    ###########################################################

    def assert_invalid_env_name(self, name):
        with self.assertRaises(ValueError):
            url_by_name(name)

    def test_valid_environment_variables(self):
        envs = ["MY_URL", "A", "FOO", "TEST_THIS_URL"]
        for env in envs:
            url_by_name(env)

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

    def test_equals_env(self):
        self.assertEqual(url_by_name("FOO"), url_by_name("FOO"))
        self.assertEqual(url_by_name("BAR"), url_by_name("BAR"))
        self.assertEqual(url_by_name("BAZ"), url_by_name("BAZ"))
        self.assertEqual(url_by_name("MY_VARIABLE"), url_by_name("MY_VARIABLE"))
        self.assertEqual(url_by_name("SOME_OTHER_VARIABLE"), url_by_name("SOME_OTHER_VARIABLE"))

    def test_unequal_env(self):
        self.assertNotEqual(url_by_name("FOO"), url_by_name("BAR"))
        self.assertNotEqual(url_by_name("MY_VARIABLE"), url_by_name("SOME_OTHER_VARIABLE"))

    ###########################################################
    # Hash
    ###########################################################

    def test_hash_1(self):
        self.assertEqual(2, len({self.url1, self.url2}))

    def test_hash_2(self):
        self.assertEqual(1, len({self.url1, self.url1}))

    def test_hash3(self):
        self.assertEqual(hash(url_by_name('FOO')), hash(url_by_name('FOO')))

    ###########################################################
    # Check
    ###########################################################
    def test_check_true(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value'}):
            self.assertTrue(url_by_name('FOO_BAR').check())

    def test_check_false(self):
        with patch.dict('os.environ', {}):
            self.assertFalse(url_by_name('FOO_BAR').check())

    ###########################################################
    # __str__ and __repr__
    ###########################################################
    def test_str(self):
        self.assertEqual('Url[name=FOO]', str(self.url1))
        self.assertEqual('Url[name=BAR]', str(self.url2))

    def test_repr(self):
        self.assertEqual('Url[name=FOO]', repr(self.url1))
        self.assertEqual('Url[name=BAR]', repr(self.url2))

    ###########################################################
    # Copy
    ###########################################################
    def test_copy_1(self):
        c1 = self.url1.copy()
        c2 = self.url2.copy()
        self.assertEqual(c1, self.url1)
        self.assertEqual(c2, self.url2)

    def test_copy_2(self):
        c1 = copy(self.url1)
        c2 = copy(self.url2)
        self.assertEqual(self.url1, c1)
        self.assertEqual(self.url2, c2)

    def test_copy_3(self):
        c1 = deepcopy(self.url1)
        c2 = deepcopy(self.url2)
        self.assertEqual(c1, self.url1)
        self.assertEqual(c2, self.url2)

    ###########################################################
    # get_value
    ###########################################################
    def test_get_value_1(self):
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.assertEqual(self.url1.get_value(), 'value1')

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAZ': 'value2'}):
            self.assertEqual(url_by_name('BAZ').get_value(), 'value2')

    ###########################################################
    # type
    ###########################################################
    def test_type_1(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.url1.type
        self.assertEqual(expect, actual)

    def test_type_2(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.url2.type
        self.assertEqual(expect, actual)

    ###########################################################
    # display
    ###########################################################
    def test_display_1(self):
        expect = 'environmentVariable'
        actual = self.url1.display
        self.assertEqual(expect, actual)

    def test_display_2(self):
        expect = 'environmentVariable'
        actual = self.url2.display
        self.assertEqual(expect, actual)

    ###########################################################
    # data
    ###########################################################
    def test_data_1(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'FOO', 'check': False}
        actual = self.url1.data
        self.assertDictEqual(expect, actual)

    def test_data_2(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'BAR', 'check': False}
        actual = self.url2.data
        self.assertDictEqual(expect, actual)

    ###########################################################
    # dict
    ###########################################################
    def test_dict_1(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'FOO', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.url1.dict()
        self.assertDictEqual(expect, actual)

    def test_dict_2(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'BAR', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.url2.dict()
        self.assertDictEqual(expect, actual)

    ###########################################################
    # target
    ###########################################################
    def test_target_1(self):
        expect = 'http://schema.org/URL'
        actual = self.url1.target
        self.assertEqual(expect, actual)

    def test_target_2(self):
        expect = 'http://schema.org/URL'
        actual = self.url2.target
        self.assertEqual(expect, actual)


class TokenEnvironmentVariablePropertyTests(unittest.TestCase):

    def setUp(self):
        self.token1 = token_by_name('FOO')
        self.token2 = token_by_name('BAR')

    ###########################################################
    # Invalid arguments to URLEnvironmentVariable
    ###########################################################
    def test_invalid_token_1(self):
        with self.assertRaises(TypeError):
            token_by_name(True)

    def test_invalid_token_2(self):
        with self.assertRaises(TypeError):
            token_by_name({})

    def test_invalid_token_3(self):
        with self.assertRaises(TypeError):
            token_by_name([])

    def test_invalid_token_4(self):
        with self.assertRaises(ValueError):
            token_by_name('ldj')

    def test_invalid_token_5(self):
        with self.assertRaises(ValueError):
            token_by_name(None)

    ###########################################################
    # Valid and invalid environment variable names
    ###########################################################

    def assert_invalid_env_name(self, name):
        with self.assertRaises(ValueError):
            token_by_name(name)

    def test_valid_environment_variables(self):
        envs = ["MY_URL", "A", "FOO", "TEST_THIS_URL"]
        for env in envs:
            token_by_name(env)

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

    # ###########################################################
    # # Equals and not equals
    # ###########################################################
    #
    def test_equals_env(self):
        self.assertEqual(token_by_name("FOO"), token_by_name("FOO"))
        self.assertEqual(token_by_name("BAR"), token_by_name("BAR"))
        self.assertEqual(token_by_name("BAZ"), token_by_name("BAZ"))
        self.assertEqual(token_by_name("MY_VARIABLE"), token_by_name("MY_VARIABLE"))
        self.assertEqual(token_by_name("SOME_OTHER_VARIABLE"), token_by_name("SOME_OTHER_VARIABLE"))

    def test_unequal_env(self):
        self.assertNotEqual(token_by_name("FOO"), token_by_name("BAR"))
        self.assertNotEqual(token_by_name("MY_VARIABLE"), token_by_name("SOME_OTHER_VARIABLE"))

    # ###########################################################
    # # Hash
    # ###########################################################
    #
    def test_hash_1(self):
        self.assertEqual(2, len({self.token1, self.token2}))

    def test_hash_2(self):
        self.assertEqual(1, len({self.token1, self.token1}))

    def test_hash3(self):
        self.assertEqual(hash(token_by_name('FOO')), hash(token_by_name('FOO')))

    # ###########################################################
    # # Check
    # ###########################################################
    def test_check_true(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value'}):
            self.assertTrue(token_by_name('FOO_BAR').check())

    def test_check_false(self):
        with patch.dict('os.environ', {}):
            self.assertFalse(token_by_name('FOO_BAR').check())

    ###########################################################
    # # __str__ and __repr__
    # ###########################################################
    def test_str(self):
        self.assertEqual('Token[name=FOO]', str(self.token1))
        self.assertEqual('Token[name=BAR]', str(self.token2))

    def test_repr(self):
        self.assertEqual('Token[name=FOO]', repr(self.token1))
        self.assertEqual('Token[name=BAR]', repr(self.token2))

    # ###########################################################
    # # Copy
    # ###########################################################
    def test_copy_1(self):
        c1 = self.token1.copy()
        c2 = self.token2.copy()
        self.assertEqual(c1, self.token1)
        self.assertEqual(c2, self.token2)

    def test_copy_2(self):
        c1 = copy(self.token1)
        c2 = copy(self.token2)
        self.assertEqual(self.token1, c1)
        self.assertEqual(self.token2, c2)

    def test_copy_3(self):
        c1 = deepcopy(self.token1)
        c2 = deepcopy(self.token2)
        self.assertEqual(c1, self.token1)
        self.assertEqual(c2, self.token2)

    # ###########################################################
    # # get_value
    # ###########################################################
    def test_get_value_1(self):
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.assertEqual(self.token1.get_value(), 'value1')

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAZ': 'value2'}):
            self.assertEqual(token_by_name('BAZ').get_value(), 'value2')

    # ###########################################################
    # # type
    # ###########################################################
    def test_type_1(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.token1.type
        self.assertEqual(expect, actual)

    def test_type_2(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.token2.type
        self.assertEqual(expect, actual)

    # ###########################################################
    # # display
    # ###########################################################
    def test_display_1(self):
        expect = 'environmentVariable'
        actual = self.token1.display
        self.assertEqual(expect, actual)

    def test_display_2(self):
        expect = 'environmentVariable'
        actual = self.token2.display
        self.assertEqual(expect, actual)

    # ###########################################################
    # # data
    # ###########################################################
    def test_data_1(self):
        expect = {'target': 'token', 'name': 'FOO', 'check': False}
        actual = self.token1.data
        self.assertDictEqual(expect, actual)

    def test_data_2(self):
        expect = {'target': 'token', 'name': 'BAR', 'check': False}
        actual = self.token2.data
        self.assertDictEqual(expect, actual)

    # ###########################################################
    # # dict
    # ###########################################################
    def test_dict_1(self):
        expect = {'target': 'token', 'name': 'FOO', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.token1.dict()
        self.assertDictEqual(expect, actual)

    def test_dict_2(self):
        expect = {'target': 'token', 'name': 'BAR', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.token2.dict()
        self.assertDictEqual(expect, actual)

    # ###########################################################
    # # target
    # ###########################################################
    def test_target_1(self):
        expect = 'token'
        actual = self.token1.target
        self.assertEqual(expect, actual)

    def test_target_2(self):
        expect = 'token'
        actual = self.token2.target
        self.assertEqual(expect, actual)


class EnumEnvironmentVariablePropertyTests(unittest.TestCase):

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
        with self.assertRaises(ValueError):
            enum_by_name(name, ["SINGLETON"])

    def test_valid_environment_variables(self):
        envs = ["MY_URL", "A", "FOO", "TEST_THIS_URL"]
        for env in envs:
            enum_by_name(env, ["SINGLETON"])

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
    def test_equals_env(self):
        choices = ['SINGLETON']
        self.assertEqual(enum_by_name("FOO", choices), enum_by_name("FOO", choices))
        self.assertEqual(enum_by_name("BAR", choices), enum_by_name("BAR", choices))
        self.assertEqual(enum_by_name("BAZ", choices), enum_by_name("BAZ", choices))
        self.assertEqual(enum_by_name("MY_VARIABLE", choices), enum_by_name("MY_VARIABLE", choices))
        self.assertEqual(enum_by_name("SOME_OTHER_VARIABLE", choices), enum_by_name("SOME_OTHER_VARIABLE", choices))

    def test_unequal_env_by_name(self):
        # Unequal by name
        choices = ['SINGLETON']
        self.assertNotEqual(enum_by_name("FOO", choices), enum_by_name("BAR", choices))
        self.assertNotEqual(enum_by_name("MY_VARIABLE", choices), enum_by_name("SOME_OTHER_VARIABLE", choices))

    def test_unequal_env_by_choices(self):
        name = 'FOO'
        self.assertNotEqual(enum_by_name(name, ['SINGLETON']), enum_by_name(name, ['FOO', 'BAR']))
        self.assertNotEqual(enum_by_name(name, ['FOO', 'BAR']), enum_by_name(name, ['ARG1', 'ARG2']))

    def test_unequal_env_by_name_and_choices(self):
        self.assertNotEqual(enum_by_name('BLA', ['SINGLETON']), enum_by_name('BLUB', ['FOO', 'BAR']))
        self.assertNotEqual(enum_by_name('BLA', ['FOO', 'BAR']), enum_by_name('BLUB', ['ARG1', 'ARG2']))

    ###########################################################
    # Hash
    ###########################################################

    def test_hash_1(self):
        self.assertEqual(2, len({self.enum1, self.enum2}))

    def test_hash_2(self):
        self.assertEqual(1, len({self.enum1, self.enum1}))

    def test_hash3(self):
        choices = ['SINGLETON']
        self.assertEqual(hash(enum_by_name('FOO', choices)), hash(enum_by_name('FOO', choices)))

    ###########################################################
    # Check
    ###########################################################
    def test_check_true_1(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value'}):
            self.assertTrue(enum_by_name('FOO_BAR', ['value']).check())

    def test_check_true_2(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value1'}):
            self.assertTrue(enum_by_name('FOO_BAR', ['value1', 'value2']).check())

    def test_check_false_when_env_var_is_missing(self):
        with patch.dict('os.environ', {}):
            self.assertFalse(enum_by_name('FOO_BAR', ['value']).check())

    def test_check_false_when_value_is_not_allowed(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value1'}):
            self.assertFalse(enum_by_name('FOO_BAR', ['value2']).check())

    ###########################################################
    # __str__ and __repr__
    ###########################################################
    def test_str(self):
        self.assertEqual('Enum[name=FOO,choices=[\'VALUE1\', \'VALUE2\']]', str(self.enum1))
        self.assertEqual('Enum[name=BAR,choices=[\'SINGLETON\']]', str(self.enum2))

    def test_repr(self):
        self.assertEqual('Enum[name=FOO,choices=[\'VALUE1\', \'VALUE2\']]', repr(self.enum1))
        self.assertEqual('Enum[name=BAR,choices=[\'SINGLETON\']]', repr(self.enum2))

    ###########################################################
    # Copy
    ###########################################################
    def test_copy_1(self):
        c1 = self.enum1.copy()
        c2 = self.enum2.copy()
        self.assertEqual(c1, self.enum1)
        self.assertEqual(c2, self.enum2)

    def test_copy_2(self):
        c1 = copy(self.enum1)
        c2 = copy(self.enum2)
        self.assertEqual(self.enum1, c1)
        self.assertEqual(self.enum2, c2)

    def test_copy_3(self):
        c1 = deepcopy(self.enum1)
        c2 = deepcopy(self.enum2)
        self.assertEqual(c1, self.enum1)
        self.assertEqual(c2, self.enum2)

    ###########################################################
    # get_value
    ###########################################################
    def test_get_value_1(self):
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.assertEqual(self.enum1.get_value(), 'value1')

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAZ': 'value2'}):
            self.assertEqual(enum_by_name('BAZ', ['value2']).get_value(), 'value2')

    ###########################################################
    # type
    ###########################################################
    def test_type_1(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.enum1.type
        self.assertEqual(expect, actual)

    def test_type_2(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.enum2.type
        self.assertEqual(expect, actual)

    ###########################################################
    # display
    ###########################################################
    def test_display_1(self):
        expect = 'environmentVariable'
        actual = self.enum1.display
        self.assertEqual(expect, actual)

    def test_display_2(self):
        expect = 'environmentVariable'
        actual = self.enum2.display
        self.assertEqual(expect, actual)

    ###########################################################
    # data
    ###########################################################
    def test_data_1(self):
        expect = {'target': 'enum', 'name': 'FOO', 'check': False}
        actual = self.enum1.data
        self.assertDictEqual(expect, actual)

    def test_data_2(self):
        expect = {'target': 'enum', 'name': 'BAR', 'check': False}
        actual = self.enum2.data
        self.assertDictEqual(expect, actual)

    ###########################################################
    # dict
    ###########################################################
    def test_dict_1(self):
        expect = {'target': 'enum', 'name': 'FOO', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.enum1.dict()
        self.assertDictEqual(expect, actual)

    def test_dict_2(self):
        expect = {'target': 'enum', 'name': 'BAR', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.enum2.dict()
        self.assertDictEqual(expect, actual)

    ###########################################################
    # target
    ###########################################################
    def test_target_1(self):
        expect = 'enum'
        actual = self.enum1.target
        self.assertEqual(expect, actual)

    def test_target_2(self):
        expect = 'enum'
        actual = self.enum2.target
        self.assertEqual(expect, actual)
