from pht.internal.response.run.rebase import DockerRebaseStrategy
from tests.base import BaseTest
from copy import copy, deepcopy


class DockerRebaseStrategyTests(BaseTest):

    def setUp(self):
        self.rebase1 = DockerRebaseStrategy('from', ['station.2'], [])

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect='DockerRebaseStrategy',
            actual=self.rebase1.type)

    ################################################################################
    # Display
    ################################################################################
    def test_display_1(self):
        self.checkExpect(
            expect='DockerRebaseStrategy',
            actual=self.rebase1.type_name)

    ################################################################################
    # Data
    ################################################################################
    def test_data_1(self):
        self.checkExpect(
            expect={'exportFiles': [], 'nextTrainTags': ['station.2'], 'from': 'from'},
            actual=self.rebase1.data)

    ################################################################################
    # Dict
    ################################################################################
    def test_dict_1(self):
        self.checkExpect(
            expect={
                'exportFiles': [],
                'nextTrainTags': ['station.2'],
                'from': 'from',
                '@type': 'DockerRebaseStrategy',
                '@typeName': 'DockerRebaseStrategy',
                "@typeSystem": "pythonclass"},
            actual=self.rebase1._as_dict())

    ################################################################################
    # Copy, deepcopy, hash
    ################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqual(self.rebase1)
