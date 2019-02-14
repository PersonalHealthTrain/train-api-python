from tests.base import BaseTest
from pht.internal.response.run.exit.RunExit import AlgorithmFailure
from pht.internal.response.run.rebase.RebaseStrategy import DockerRebaseStrategy
from pht.internal.response.run.RunResponse import RunResponse


class RunResponseTests(BaseTest):

    def setUp(self):
        self.response = RunResponse(
            run_exit=AlgorithmFailure('foo'),
            free_text_message='bar',
            rebase=DockerRebaseStrategy(
                frm='frm',
                next_train_tags=['tag1', 'tag2'],
                export_files=[]
            ))

    ################################################################################
    # As Dict
    ################################################################################
    def test_as_dict_1(self):
        self.checkExpect(
            expect={
                'version': '1.0',
                'exit': {'state': 'failure', 'reason': 'foo'},
                'free_text_message': 'bar',
                'rebase': {
                    'export_files': [],
                    'next_train_tags': ['tag1', 'tag2'],
                    'from': 'frm',
                    'type': 'docker',
                    'display': 'docker'
                },
                'type': 'RunResponse',
                'display': 'RunResponse'},
            actual=self.response.as_dict()
        )

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response.type)

    ################################################################################
    # Display
    ################################################################################
    def test_display_1(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response.display)

    ################################################################################
    # Data
    ################################################################################
    def test_data_1(self):
        self.checkExpect(
            expect={
                'version': '1.0',
                'exit': {'state': 'failure', 'reason': 'foo'},
                'free_text_message': 'bar',
                'rebase': {
                    'export_files': [],
                    'next_train_tags': ['tag1', 'tag2'],
                    'from': 'frm',
                    'type': 'docker',
                    'display': 'docker'}
            },
            actual=self.response.data)
