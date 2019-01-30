import unittest
from unittest.mock import patch
from copy import copy, deepcopy
from pht.internal.describe.property import TokenEnvironmentVariableProperty, UrlEnvironmentVariableProperty


def _env(name):
    return UrlEnvironmentVariableProperty(name)


def _token(name):
    return TokenEnvironmentVariableProperty(name)


class UrlEnvironmentVariablePropertyTests(unittest.TestCase):

    def setUp(self):
        self.env1 = _env('FOO')
        self.env2 = _env('BAR')

    ###########################################################
    # Invalid arguments to URLEnvironmentVariable
    ###########################################################
    def test_invalid_url_1(self):
        with self.assertRaises(TypeError):
            _env(True)

    def test_invalid_url_2(self):
        with self.assertRaises(TypeError):
            _env({})

    def test_invalid_url_3(self):
        with self.assertRaises(TypeError):
            _env([])

    def test_invalid_url_4(self):
        with self.assertRaises(ValueError):
            _env('ldj')

    def test_invalid_url_5(self):
        with self.assertRaises(ValueError):
            _env(None)

    ###########################################################
    # Valid and invalid environment variable names
    ###########################################################

    def assert_invalid_env_name(self, name):
        with self.assertRaises(ValueError):
            _env(name)

    def test_valid_environment_variables(self):
        envs = ["MY_URL", "A", "FOO", "TEST_THIS_URL"]
        for env in envs:
            _env(env)

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
        self.assertEqual(_env("FOO"), _env("FOO"))
        self.assertEqual(_env("BAR"), _env("BAR"))
        self.assertEqual(_env("BAZ"), _env("BAZ"))
        self.assertEqual(_env("MY_VARIABLE"), _env("MY_VARIABLE"))
        self.assertEqual(_env("SOME_OTHER_VARIABLE"), _env("SOME_OTHER_VARIABLE"))

    def test_unequal_env(self):
        self.assertNotEqual(_env("FOO"), _env("BAR"))
        self.assertNotEqual(_env("MY_VARIABLE"), _env("SOME_OTHER_VARIABLE"))

    ###########################################################
    # Hash
    ###########################################################

    def test_hash_1(self):
        self.assertEqual(2, len({self.env1, self.env2}))

    def test_hash_2(self):
        self.assertEqual(1, len({self.env1, self.env1}))

    def test_hash3(self):
        self.assertEqual(hash(_env('FOO')), hash(_env('FOO')))

    ###########################################################
    # Check
    ###########################################################
    def test_check_true(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value'}):
            self.assertTrue(_env('FOO_BAR').check())

    def test_check_false(self):
        with patch.dict('os.environ', {}):
            self.assertFalse(_env('FOO_BAR').check())

    ###########################################################
    # __str__ and __repr__
    ###########################################################
    def test_str(self):
        self.assertEqual('Url[name=FOO]', str(self.env1))
        self.assertEqual('Url[name=BAR]', str(self.env2))

    def test_repr(self):
        self.assertEqual('Url[name=FOO]', repr(self.env1))
        self.assertEqual('Url[name=BAR]', repr(self.env2))

    ###########################################################
    # Copy
    ###########################################################
    def test_copy_1(self):
        c1 = self.env1.copy()
        c2 = self.env2.copy()
        self.assertEqual(c1, self.env1)
        self.assertEqual(c2, self.env2)

    def test_copy_2(self):
        c1 = copy(self.env1)
        c2 = copy(self.env2)
        self.assertEqual(self.env1, c1)
        self.assertEqual(self.env2, c2)

    def test_copy_3(self):
        c1 = deepcopy(self.env1)
        c2 = deepcopy(self.env2)
        self.assertEqual(c1, self.env1)
        self.assertEqual(c2, self.env2)

    ###########################################################
    # get_value
    ###########################################################
    def test_get_value_1(self):
        with patch.dict('os.environ', {'FOO': 'value1'}):
            self.assertEqual(self.env1.get_value(), 'value1')

    def test_get_value_2(self):
        with patch.dict('os.environ', {'BAZ': 'value2'}):
            self.assertEqual(_env('BAZ').get_value(), 'value2')

    ###########################################################
    # type
    ###########################################################
    def test_type_1(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.env1.type
        self.assertEqual(expect, actual)

    def test_type_2(self):
        expect = 'http://www.wikidata.org/entity/Q400857'
        actual = self.env2.type
        self.assertEqual(expect, actual)

    ###########################################################
    # display
    ###########################################################
    def test_display_1(self):
        expect = 'environmentVariable'
        actual = self.env1.display
        self.assertEqual(expect, actual)

    def test_display_2(self):
        expect = 'environmentVariable'
        actual = self.env2.display
        self.assertEqual(expect, actual)

    ###########################################################
    # data
    ###########################################################
    def test_data_1(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'FOO', 'check': False}
        actual = self.env1.data
        self.assertDictEqual(expect, actual)

    def test_data_2(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'BAR', 'check': False}
        actual = self.env2.data
        self.assertDictEqual(expect, actual)

    ###########################################################
    # dict
    ###########################################################
    def test_dict_1(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'FOO', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.env1.dict()
        self.assertDictEqual(expect, actual)

    def test_dict_2(self):
        expect = {'target': 'http://schema.org/URL', 'name': 'BAR', 'check': False, 'type': 'http://www.wikidata.org/entity/Q400857', 'display': 'environmentVariable'}
        actual = self.env2.dict()
        self.assertDictEqual(expect, actual)

    ###########################################################
    # target
    ###########################################################
    def test_target_1(self):
        expect = 'http://schema.org/URL'
        actual = self.env1.target
        self.assertEqual(expect, actual)

    def test_target_2(self):
        expect = 'http://schema.org/URL'
        actual = self.env2.target
        self.assertEqual(expect, actual)


class TokenEnvironmentVariablePropertyTests(unittest.TestCase):

    def setUp(self):
        self.token1 = _token('FOO')
        self.token2 = _token('BAR')

    ###########################################################
    # Invalid arguments to URLEnvironmentVariable
    ###########################################################
    def test_invalid_token_1(self):
        with self.assertRaises(TypeError):
            _token(True)

    def test_invalid_token_2(self):
        with self.assertRaises(TypeError):
            _token({})

    def test_invalid_token_3(self):
        with self.assertRaises(TypeError):
            _token([])

    def test_invalid_token_4(self):
        with self.assertRaises(ValueError):
            _token('ldj')

    def test_invalid_token_5(self):
        with self.assertRaises(ValueError):
            _token(None)

    ###########################################################
    # Valid and invalid environment variable names
    ###########################################################

    def assert_invalid_env_name(self, name):
        with self.assertRaises(ValueError):
            _token(name)

    def test_valid_environment_variables(self):
        envs = ["MY_URL", "A", "FOO", "TEST_THIS_URL"]
        for env in envs:
            _token(env)

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
        self.assertEqual(_token("FOO"), _token("FOO"))
        self.assertEqual(_token("BAR"), _token("BAR"))
        self.assertEqual(_token("BAZ"), _token("BAZ"))
        self.assertEqual(_token("MY_VARIABLE"), _token("MY_VARIABLE"))
        self.assertEqual(_token("SOME_OTHER_VARIABLE"), _token("SOME_OTHER_VARIABLE"))

    def test_unequal_env(self):
        self.assertNotEqual(_token("FOO"), _token("BAR"))
        self.assertNotEqual(_token("MY_VARIABLE"), _token("SOME_OTHER_VARIABLE"))

    # ###########################################################
    # # Hash
    # ###########################################################
    #
    def test_hash_1(self):
        self.assertEqual(2, len({self.token1, self.token2}))

    def test_hash_2(self):
        self.assertEqual(1, len({self.token1, self.token1}))

    def test_hash3(self):
        self.assertEqual(hash(_token('FOO')), hash(_token('FOO')))

    # ###########################################################
    # # Check
    # ###########################################################
    def test_check_true(self):
        with patch.dict('os.environ', {'FOO_BAR': 'value'}):
            self.assertTrue(_token('FOO_BAR').check())

    def test_check_false(self):
        with patch.dict('os.environ', {}):
            self.assertFalse(_token('FOO_BAR').check())

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
            self.assertEqual(_token('BAZ').get_value(), 'value2')

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
