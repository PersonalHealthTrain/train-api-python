from tests.base import BaseTest
from pht.internal.train.cargo.AlgorithmFile import AlgorithmFile


class AlgorithmFileTests(BaseTest):

    def setUp(self):
        self.algo_file1 = AlgorithmFile('foo')
        self.algo_file2 = AlgorithmFile('bar')

    ###########################################
    # Invalid Model key names
    ###########################################
    def test_eq_1(self):
        self.assertIsEqual(self.algo_file1, AlgorithmFile('foo'))

    def test_eq_2(self):
        self.assertIsEqual(self.algo_file2, AlgorithmFile('bar'))

    def test_unequal(self):
        self.assertNotEqual(self.algo_file1, self.algo_file2)

    ###########################################
    # Type
    ###########################################
    def test_type_1(self):
        self.checkExpect(
            expect=['AlgorithmFile', 'TrainFile'],
            actual=self.algo_file1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=['AlgorithmFile', 'TrainFile'],
            actual=self.algo_file2.type)

    ###########################################
    # Display
    ###########################################
    def test_type_name_1(self):
        self.checkExpect(
            expect='AlgorithmFile',
            actual=self.algo_file1.type_name)

    def test_type_name_2(self):
        self.checkExpect(
            expect='AlgorithmFile',
            actual=self.algo_file2.type_name)

    ###########################################
    # Data
    ###########################################
    def test_data_1(self):
        self.checkExpect(
            expect={'absolutePath': '/opt/pht_train/algorithm/foo'},
            actual=self.algo_file1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={'absolutePath': '/opt/pht_train/algorithm/bar'},
            actual=self.algo_file2.data)

    ###########################################
    # as dict
    ###########################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={\
                'absolutePath': '/opt/pht_train/algorithm/foo',
                '@type': ['AlgorithmFile', 'TrainFile'],
                '@typeName': 'AlgorithmFile',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.algo_file1.as_simple_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'absolutePath': '/opt/pht_train/algorithm/bar',
                '@type': ['AlgorithmFile', 'TrainFile'],
                '@typeName': 'AlgorithmFile',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.algo_file2.as_simple_dict())

    ###########################################
    # absolute path
    ###########################################
    def test_absolute_path_1(self):
        self.checkExpect(
            expect='/opt/pht_train/algorithm/foo',
            actual=self.algo_file1.absolute_path)

    def test_absolute_path_2(self):
        self.checkExpect(
            expect='/opt/pht_train/algorithm/bar',
            actual=self.algo_file2.absolute_path)

    ###########################################
    # total ordering
    ###########################################
    def test_ordering_1(self):
        self.assertLess(self.algo_file2, self.algo_file1)

    def test_ordering_2(self):
        self.assertLessEqual(self.algo_file2, self.algo_file1)

    def test_ordering_3(self):
        self.assertGreater(self.algo_file1, self.algo_file2)

    def test_ordering_4(self):
        self.assertGreaterEqual(self.algo_file1, self.algo_file2)
