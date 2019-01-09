import unittest

from pht.response.requirement import req_url
from pht.response.requirement.clause import require_any, require_all
from pht.response import ListRequirementsResponse


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


class ListRequirementsResponseTests(unittest.TestCase):

    def test_serialize_response_1(self):
        response = ListRequirementsResponse(require_all(req_url('FOO'))).to_json_string()
        string = '{"requirements":' \
                 ' [{"id": 0, "requirement": {"type": "environmentVariable", "target": "URL", "name": "FOO"}}], ' \
                 '"clauses": [{"id": 0, "type": "all", "requirements": [0]}]}'
        self.assertEqual(response, string)

    def test_serialize_response_2(self):
        requirements = require_all(req_url('FOO'), req_url('BAR')) + require_any(req_url('BAZ'))
        response = ListRequirementsResponse(requirements).to_json_string()
        string = '{"requirements":' \
                 ' [{"id": 0, "requirement": {"type": "environmentVariable", "target": "URL", "name": "FOO"}},' \
                 ' {"id": 1, "requirement": {"type": "environmentVariable", "target": "URL", "name": "BAR"}},' \
                 ' {"id": 2, "requirement": {"type": "environmentVariable", "target": "URL", "name": "BAZ"}}],' \
                 ' "clauses": [{"id": 0, "type": "all", "requirements": [0, 1]},' \
                 ' {"id": 1, "type": "any", "requirements": [2]}]}'
        self.assertEqual(response, string)

    def test_serialize_response_3(self):
        requirements = require_any(req_url('BAZ'), req_url('BAM'))\
                       + require_all(req_url('FOO_BAR'))\
                       + require_any(req_url('FOO'))
        response = ListRequirementsResponse(requirements).to_json_string()
        string = '{"requirements": ' \
                 '[{"id": 0, "requirement": {"type": "environmentVariable", "target": "URL", "name": "BAZ"}},' \
                 ' {"id": 1, "requirement": {"type": "environmentVariable", "target": "URL", "name": "BAM"}},' \
                 ' {"id": 2, "requirement": {"type": "environmentVariable", "target": "URL", "name": "FOO_BAR"}},' \
                 ' {"id": 3, "requirement": {"type": "environmentVariable", "target": "URL", "name": "FOO"}}],' \
                 ' "clauses": [{"id": 0, "type": "any", "requirements": [0, 1]},' \
                 ' {"id": 1, "type": "all", "requirements": [2]}, {"id": 2, "type": "any", "requirements": [3]}]}'
        self.assertEqual(string, response)


if __name__ == '__main__':
    unittest.main()
