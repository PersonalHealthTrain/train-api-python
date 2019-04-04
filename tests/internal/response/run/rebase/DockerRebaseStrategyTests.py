from pht.internal.response.run.rebase import DockerRebaseStrategy
from tests.base import BaseTest


class DockerRebaseStrategyTests(BaseTest):

    def setUp(self):
        self.rebase1 = DockerRebaseStrategy('from', ['station.2'], [])

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect=['DockerRebaseStrategy', 'RebaseStrategy'],
            actual=self.rebase1.type)

    ################################################################################
    # Display
    ################################################################################
    def test_type_name_1(self):
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
    def test_simple_dict_1(self):
        self.checkMapping(
            expect={
                'exportFiles': [],
                'nextTrainTags': ['station.2'],
                'from': 'from',
                '@type': ['DockerRebaseStrategy', 'RebaseStrategy'],
                '@typeName': 'DockerRebaseStrategy',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                }
            },
            actual=self.rebase1.as_simple_mapping())

    ################################################################################
    # Copy, deepcopy, hash
    ################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.rebase1)
