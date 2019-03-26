from tests.base import BaseTest
from pht.internal.train.cargo.ModelFile import ModelFile


class TrainFileTests(BaseTest):

    def setUp(self):
        self.modelfile1 = ModelFile('foo')
        self.modelfile2 = ModelFile('bar')

    ########################################################
    # Value Error
    ########################################################
    def test_value_error_1(self):
        self.assertValueError(lambda: ModelFile(''))

    def test_value_error_2(self):
        self.assertValueError(lambda: ModelFile(' '))

    def test_value_error_3(self):
        self.assertValueError(lambda: ModelFile('foo/bar'))

    def test_value_error_4(self):
        self.assertValueError(lambda: ModelFile('foo\\bar'))

    ########################################################
    # eq
    ########################################################
    def test_eq_1(self):
        self.assertIsEqual(self.modelfile1, ModelFile('foo'))

    def test_eq_2(self):
        self.assertIsEqual(self.modelfile2, ModelFile('bar'))

    ########################################################
    # path
    ########################################################
    def test_path_1(self):
        self.checkExpect(
            expect='/opt/pht_train/model/foo',
            actual=self.modelfile1.absolute_path)

    def test_path_2(self):
        self.checkExpect(
            expect='/opt/pht_train/model/bar',
            actual=self.modelfile2.absolute_path)

    ########################################################
    # type
    ########################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['ModelFile', 'TrainFile'],
            actual=self.modelfile1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['ModelFile', 'TrainFile'],
            actual=self.modelfile2.type)

    ########################################################
    # display
    ########################################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='ModelFile',
            actual=self.modelfile1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='ModelFile',
            actual=self.modelfile2.type_name)

    ########################################################
    # data
    ########################################################
    def test_data_1(self):
        self.checkExpect(
            expect={
                'absolutePath': '/opt/pht_train/model/foo'
            },
            actual=self.modelfile1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={
                'absolutePath': '/opt/pht_train/model/bar'
            },
            actual=self.modelfile2.data)

    ########################################################
    # as_dict
    ########################################################
    def test_as_simple_dict_1(self):
        self.checkExpect(
            expect={
                'absolutePath': '/opt/pht_train/model/foo',
                '@type': ['ModelFile', 'TrainFile'],
                '@typeName': 'ModelFile',
                '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                }
            },
            actual=self.modelfile1._as_dict())  # TODO Check that in assertion test

    def test_as_simple_dict_2(self):
        self.checkExpect(
            expect={
                'absolutePath': '/opt/pht_train/model/bar',
                '@type': ['ModelFile', 'TrainFile'],
                '@typeName': 'ModelFile',
                '@typeSystem': {
                        'name': 'pythonclass',
                        'version': '1.0'
                }
            },
            actual=self.modelfile2.as_simple_dict())
