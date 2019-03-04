from tests.base import BaseTest
from pht.internal.response.describe.model.StringModelSummary import StringModelSummary


class StringModelSummaryTests(BaseTest):

    def setUp(self):
        self.model1 = StringModelSummary('This is the model summary')
        self.model2 = StringModelSummary('This is another model summary')

    ##############################################################
    # Type Error
    ##############################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: StringModelSummary())

    def test_type_error_2(self):
        self.assertTypeError(lambda: StringModelSummary(1))

    def test_type_error_3(self):
        self.assertTypeError(lambda: StringModelSummary(True))

    def test_type_error_4(self):
        self.assertTypeError(lambda: StringModelSummary(None))

    def test_type_error_5(self):
        self.assertTypeError(lambda: StringModelSummary(0.7264))

    ##############################################################
    # __eq__
    ##############################################################
    def test_eq_1(self):
        self.assertIsEqual(self.model1, StringModelSummary('This is the model summary'))

    def test_eq_2(self):
        self.assertIsEqual(self.model2, StringModelSummary('This is another model summary'))

    def test_unequal(self):
        self.assertNotEqual(self.model1, self.model2)

    ##############################################################
    # copy
    ##############################################################
    def test_copy_1(self):
        self.assertCopiesAreEqual(self.model1)

    def test_copy_2(self):
        self.assertCopiesAreEqual(self.model2)

    ##############################################################
    # type
    ##############################################################
    def test_type_1(self):
        self.checkExpect(
            expect='StringModelSummary',
            actual=self.model1.type)

    def test_type_2(self):
        self.checkExpect(
            expect='StringModelSummary',
            actual=self.model2.type)

    ##############################################################
    # typeName
    ##############################################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='StringModelSummary',
            actual=self.model1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='StringModelSummary',
            actual=self.model2.type_name)

    ##############################################################
    # value
    ##############################################################
    def test_value_1(self):
        self.checkExpect(
            expect='This is the model summary',
            actual=self.model1.value)

    def test_value_2(self):
        self.checkExpect(
            expect='This is another model summary',
            actual=self.model2.value)

    ##############################################################
    # data
    ##############################################################
    def test_data_1(self):
        self.checkExpect(
            expect={'value': 'This is the model summary'},
            actual=self.model1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'value': 'This is another model summary'},
            actual=self.model2.data)

    ##############################################################
    # as_dict
    ##############################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={
                'value': 'This is the model summary',
                'type': 'StringModelSummary',
                'typeName': 'StringModelSummary',
                'typeSystem': 'pythonclass'
            },
            actual=self.model1._as_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'value': 'This is another model summary',
                'type': 'StringModelSummary',
                'typeName': 'StringModelSummary',
                'typeSystem': 'pythonclass'
            },
            actual=self.model2._as_dict())
