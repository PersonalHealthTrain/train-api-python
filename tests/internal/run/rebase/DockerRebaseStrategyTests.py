from pht.internal.run.rebase import DockerRebaseStrategy
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
            expect='docker',
            actual=self.rebase1.type)

    ################################################################################
    # Display
    ################################################################################
    def test_display_1(self):
        self.checkExpect(
            expect='docker',
            actual=self.rebase1.display)

    ################################################################################
    # Data
    ################################################################################
    def test_data_1(self):
        self.checkExpect(
            expect={'export_files': [], 'next_train_tags': ['station.2'], 'from': 'from'},
            actual=self.rebase1.data)

    ################################################################################
    # Dict
    ################################################################################
    def test_dict_1(self):
        self.checkExpect(
            expect={'export_files': [], 'next_train_tags': ['station.2'], 'from': 'from', 'type': 'docker', 'display': 'docker'},
            actual=self.rebase1.as_dict())

    ################################################################################
    # Copy, deepcopy, hash
    ################################################################################
    def test_copy_1(self):
        c1 = copy(self.rebase1)
        c2 = self.rebase1.copy()
        c3 = deepcopy(self.rebase1)
        self.assertEqual(c1, self.rebase1)
        self.assertEqual(c2, self.rebase1)
        self.assertEqual(c3, self.rebase1)
        self.assertEqual(hash(c1), hash(self.rebase1))
        self.assertEqual(hash(c2), hash(self.rebase1))
        self.assertEqual(hash(c3), hash(self.rebase1))
