import unittest
from pht.response.requirement import req_url


class RequirementsTests(unittest.TestCase):

    # Environment Variables
    def assert_invalid_env_name(self, string: str):
        with self.assertRaises(ValueError):
            req_url(string)

    def test_valid_environment_variables(self):
        envs = ["MY_URL", "A", "FOO", "TEST_THIS_URL"]
        for env in envs:
            req_url(env)

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

    # EnvironmtVariables Requirement equals
    def test_equals_env(self):
        self.assertEqual(req_url("FOO"), req_url("FOO"))
        self.assertEqual(req_url("BAR"), req_url("BAR"))
        self.assertEqual(req_url("BAZ"), req_url("BAZ"))
        self.assertEqual(req_url("MY_VARIABLE"), req_url("MY_VARIABLE"))
        self.assertEqual(req_url("SOME_OTHER_VARIABLE"), req_url("SOME_OTHER_VARIABLE"))

    def test_unequal_env(self):
        self.assertNotEqual(req_url("FOO"), req_url("BAR"))
        self.assertNotEqual(req_url("MY_VARIABLE"), req_url("SOME_OTHER_VARIABLE"))
