import unittest
from pht.internal.response import PrintModelSummaryResponse


class PrintModelSummaryResponseTests(unittest.TestCase):

    def test_print_model_summary_1(self):
        response = PrintModelSummaryResponse('tests').to_json_string()
        test = '{"type": "PrintModelSummaryResponse", "content": "tests"}'
        self.assertEqual(response, test)

    def test_print_model_summary_2(self):
        response = PrintModelSummaryResponse('').to_json_string()
        test = '{"type": "PrintModelSummaryResponse", "content": ""}'
        self.assertEqual(response, test)
