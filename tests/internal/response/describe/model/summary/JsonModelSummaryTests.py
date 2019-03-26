import copy
from tests.base import BaseTest
from pht.internal.response.describe.model.JsonModelSummary import JsonModelSummary


class JsonModelSummaryTests(BaseTest):

    def setUp(self):
        self.model1 = JsonModelSummary({"key1": "value1", "key2": "value2"})
        self.model2 = JsonModelSummary(["entry1", "entry2"])

    def assertCopy(self, item):
        c1 = copy.copy(item)
        c2 = copy.deepcopy(item)
        self.assertEqual(c1, c2)
        self.assertEqual(c1, item)
        self.assertEqual(c2, item)
        self.assertIsNot(c1, item)
        self.assertIsNot(c2, item)

    ##############################################################
    # __eq__
    ##############################################################
    def test_eq_1(self):
        self.assertEqual(self.model1, JsonModelSummary({"key1": "value1", "key2": "value2"}))

    def test_eq_2(self):
        self.assertEqual(self.model2, JsonModelSummary(["entry1", "entry2"]))

    def test_unequal(self):
        self.assertNotEqual(self.model1, self.model2)

    ##############################################################
    # copy
    ##############################################################
    def test_copy_1(self):
        self.assertCopy(self.model1)

    def test_copy_2(self):
        self.assertCopy(self.model2)

    ##############################################################
    # type
    ##############################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['JsonModelSummary', 'ModelSummary'],
            actual=self.model1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['JsonModelSummary', 'ModelSummary'],
            actual=self.model2.type)

    ##############################################################
    # display
    ##############################################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='JsonModelSummary',
            actual=self.model1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='JsonModelSummary',
            actual=self.model2.type_name)

    ##############################################################
    # value
    ##############################################################
    def test_value_1(self):
        self.checkExpect(
            expect={
                'key1': 'value1',
                'key2': 'value2'
            },
            actual=self.model1.value)

    def test_value_2(self):
        self.checkExpect(
            expect=[
                'entry1', 'entry2'
            ],
            actual=self.model2.value)

    ##############################################################
    # data
    ##############################################################
    def test_data_1(self):
        self.checkExpect(
            expect={'value': {
                'key1': 'value1',
                'key2': 'value2'
                }
            },
            actual=self.model1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'value': ['entry1', 'entry2']},
            actual=self.model2.data)

    ##############################################################
    # as_dict
    ##############################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={
                'value': {
                    'key1': 'value1',
                    'key2': 'value2'
                },
                '@type': ['JsonModelSummary', 'ModelSummary'],
                '@typeName': 'JsonModelSummary',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.model1._as_dict())  # TODO

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'value': ['entry1', 'entry2'],
                '@type': ['JsonModelSummary', 'ModelSummary'],
                '@typeName': 'JsonModelSummary',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.model2._as_dict())  # TODO
