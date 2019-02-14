from tests.base import BaseTest
from pht.internal.train.TrainFile import TrainFile


class TrainFileTests(BaseTest):

    def setUp(self):
        self.trainfile1 = TrainFile('foo')
        self.trainfile2 = TrainFile('bar')

    ########################################################
    # Value Error
    ########################################################
    def test_value_error_1(self):
        self.assertValueError(lambda: TrainFile(''))

    def test_value_error_2(self):
        self.assertValueError(lambda: TrainFile(' '))

    def test_value_error_3(self):
        self.assertValueError(lambda: TrainFile('foo/bar'))

    def test_value_error_4(self):
        self.assertValueError(lambda: TrainFile('foo\\bar'))

    ########################################################
    # eq
    ########################################################
    def test_eq_1(self):
        self.assertIsEqual(self.trainfile1, TrainFile('foo'))

    def test_eq_2(self):
        self.assertIsEqual(self.trainfile2, TrainFile('bar'))

    ########################################################
    # path
    ########################################################
    def test_path_1(self):
        self.checkExpect(
            expect='/opt/train/foo',
            actual=self.trainfile1.path)

    def test_path_2(self):
        self.checkExpect(
            expect='/opt/train/bar',
            actual=self.trainfile2.path)

    ########################################################
    # type
    ########################################################
    def test_type_1(self):
        self.checkExpect(
            expect='TrainFile',
            actual=self.trainfile1.type)

    def test_type_2(self):
        self.checkExpect(
            expect='TrainFile',
            actual=self.trainfile2.type)

    ########################################################
    # display
    ########################################################
    def test_display_1(self):
        self.checkExpect(
            expect='TrainFile',
            actual=self.trainfile1.display)

    def test_display_2(self):
        self.checkExpect(
            expect='TrainFile',
            actual=self.trainfile2.display)

    ########################################################
    # data
    ########################################################
    def test_data_1(self):
        self.checkExpect(
            expect={'path': '/opt/train/foo'},
            actual=self.trainfile1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'path': '/opt/train/bar'},
            actual=self.trainfile2.data)

    ########################################################
    # as_dict
    ########################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={'path': '/opt/train/foo', 'type': 'TrainFile', 'display': 'TrainFile'},
            actual=self.trainfile1.as_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={'path': '/opt/train/bar', 'type': 'TrainFile', 'display': 'TrainFile'},
            actual=self.trainfile2.as_dict())
