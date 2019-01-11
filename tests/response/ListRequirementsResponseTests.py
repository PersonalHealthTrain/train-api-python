import unittest
from pht.response import ListRequirementsResponse
from pht.property import req_url
from pht.formula import require_all, require_any


class ListRequirementsResponseTests(unittest.TestCase):

    def test_serialize_response_1(self):
        response = ListRequirementsResponse(require_all(req_url('FOO'))).to_json_string()
        string = '{"type": "ListRequirementsResponse", ' \
                 '"requirements":' \
                 ' [{"id": 0, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO"}}], ' \
                 '"clauses": [{"id": 0, "type": "all", "requirements": [0]}], '\
                 '"check": false}'
        self.assertEqual(response, string)

    def test_serialize_response_2(self):
        requirements = require_all(req_url('FOO'), req_url('BAR')) + require_any(req_url('BAZ'))
        response = ListRequirementsResponse(requirements).to_json_string()
        string = '{"type": "ListRequirementsResponse", '\
                 '"requirements":' \
                 ' [{"id": 0, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO"}},' \
                 ' {"id": 1, "property": {"type": "environmentVariable", "target": "URL", "name": "BAR"}},' \
                 ' {"id": 2, "property": {"type": "environmentVariable", "target": "URL", "name": "BAZ"}}],' \
                 ' "clauses": [{"id": 0, "type": "all", "requirements": [0, 1]},' \
                 ' {"id": 1, "type": "any", "requirements": [2]}], ' \
                 '"check": false}'
        self.assertEqual(response, string)

    def test_serialize_response_3(self):
        requirements = require_any(req_url('BAZ'), req_url('BAM'))\
                       + require_all(req_url('FOO_BAR'))\
                       + require_any(req_url('FOO'))
        response = ListRequirementsResponse(requirements).to_json_string()
        string = '{"type": "ListRequirementsResponse", '\
                 '"requirements": ' \
                 '[{"id": 0, "property": {"type": "environmentVariable", "target": "URL", "name": "BAZ"}},' \
                 ' {"id": 1, "property": {"type": "environmentVariable", "target": "URL", "name": "BAM"}},' \
                 ' {"id": 2, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO_BAR"}},' \
                 ' {"id": 3, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO"}}],' \
                 ' "clauses": [{"id": 0, "type": "any", "requirements": [0, 1]},' \
                 ' {"id": 1, "type": "all", "requirements": [2]}, {"id": 2, "type": "any", "requirements": [3]}], ' \
                 '"check": false}'
        self.assertEqual(string, response)

    def test_serialize_response_4(self):
        requirements = require_any(req_url('BAZ'), req_url('BAM'))\
                       + require_all(req_url('FOO_BAR'))\
                       + require_any(req_url('FOO'))
        unmet = [req_url('BAZ')]
        response = ListRequirementsResponse(requirements, unmet).to_json_string()
        string = '{"type": "ListRequirementsResponse", '\
                 '"requirements": ' \
                 '[{"id": 0, "property": {"type": "environmentVariable", "target": "URL", "name": "BAZ"}},' \
                 ' {"id": 1, "property": {"type": "environmentVariable", "target": "URL", "name": "BAM"}},' \
                 ' {"id": 2, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO_BAR"}},' \
                 ' {"id": 3, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO"}}],' \
                 ' "clauses": [{"id": 0, "type": "any", "requirements": [0, 1]},' \
                 ' {"id": 1, "type": "all", "requirements": [2]}, {"id": 2, "type": "any", "requirements": [3]}], ' \
                 '"check": true, "unmet": [0]}'
        self.assertEqual(string, response)

    def test_serialize_response_5(self):
        requirements = require_any(req_url('BAZ'), req_url('BAM'))\
                       + require_all(req_url('FOO_BAR'))\
                       + require_any(req_url('FOO'))
        unmet = []
        response = ListRequirementsResponse(requirements, unmet).to_json_string()
        string = '{"type": "ListRequirementsResponse", '\
                 '"requirements": ' \
                 '[{"id": 0, "property": {"type": "environmentVariable", "target": "URL", "name": "BAZ"}},' \
                 ' {"id": 1, "property": {"type": "environmentVariable", "target": "URL", "name": "BAM"}},' \
                 ' {"id": 2, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO_BAR"}},' \
                 ' {"id": 3, "property": {"type": "environmentVariable", "target": "URL", "name": "FOO"}}],' \
                 ' "clauses": [{"id": 0, "type": "any", "requirements": [0, 1]},' \
                 ' {"id": 1, "type": "all", "requirements": [2]}, {"id": 2, "type": "any", "requirements": [3]}], ' \
                 '"check": true, "unmet": []}'
        self.assertEqual(string, response)
