from tests.base import BaseTest
from pht.internal.train.cargo.ModelFile import ModelFile


class ModelFileTests(BaseTest):

    def setUp(self):
        self.model_file1 = ModelFile('foo')
        self.model_file2 = ModelFile('bar')

    ###########################################
    # Invalid Model key names
    ###########################################
    def test_invalid_key_1(self):
        self.assertValueError(lambda: ModelFile(''))

    def test_invalid_key_2(self):
        self.assertValueError(lambda: ModelFile('foo/bar'))

    ###########################################
    # Invalid Model key names
    ###########################################
    def test_eq_1(self):
        self.assertIsEqual(self.model_file1, ModelFile('foo'))

    def test_eq_2(self):
        self.assertIsEqual(self.model_file2, ModelFile('bar'))

    def test_unequal(self):
        self.assertNotEqual(self.model_file1, self.model_file2)

    ###########################################
    # Type
    ###########################################
    def test_type_1(self):
        self.checkExpect(
            expect='ModelFile',
            actual=self.model_file1.type)

    def test_type_2(self):
        self.checkExpect(
            expect='ModelFile',
            actual=self.model_file2.type)

    ###########################################
    # Display
    ###########################################
    def test_display_1(self):
        self.checkExpect(
            expect='ModelFile',
            actual=self.model_file1.type_name)

    def test_display_2(self):
        self.checkExpect(
            expect='ModelFile',
            actual=self.model_file2.type_name)

    ###########################################
    # Data
    ###########################################
    def test_data_1(self):
        self.checkExpect(
            expect={'absolutePath': '/opt/pht_train/model/foo'},
            actual=self.model_file1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'absolutePath': '/opt/pht_train/model/bar'},
            actual=self.model_file2.data)

    ###########################################
    # as dict
    ###########################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={
                'absolutePath': '/opt/pht_train/model/foo',
                'type': 'ModelFile',
                'typeName': 'ModelFile',
                "typeSystem": "pythonclass",
            },
            actual=self.model_file1._as_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'absolutePath': '/opt/pht_train/model/bar',
                'type': 'ModelFile',
                'typeName': 'ModelFile',
                "typeSystem": "pythonclass",
            },
            actual=self.model_file2._as_dict())

    ###########################################
    # absolute path
    ###########################################
    def test_absolute_path_1(self):
        self.checkExpect(
            expect='/opt/pht_train/model/foo',
            actual=self.model_file1.absolute_path)

    def test_absolute_path_2(self):
        self.checkExpect(
            expect='/opt/pht_train/model/bar',
            actual=self.model_file2.absolute_path)

    ###########################################
    # total ordering
    ###########################################
    def test_ordering_1(self):
        self.assertLess(self.model_file2, self.model_file1)

    def test_ordering_2(self):
        self.assertLessEqual(self.model_file2, self.model_file1)

    def test_ordering_3(self):
        self.assertGreater(self.model_file1, self.model_file2)

    def test_ordering_4(self):
        self.assertGreaterEqual(self.model_file1, self.model_file2)
