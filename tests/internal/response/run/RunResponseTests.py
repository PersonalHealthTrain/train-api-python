from tests.base import BaseTest
from pht.internal.response.run.exit.RunExit import AlgorithmFailure
from pht.internal.response.run.rebase.RebaseStrategy import DockerRebaseStrategy
from pht.internal.response.run.RunResponse import RunResponse
from pht.internal.train.cargo.ModelFile import ModelFile
from pht.internal.train.cargo.AlgorithmFile import AlgorithmFile


class RunResponseTests(BaseTest):

    def setUp(self):
        self.response1 = RunResponse(
            run_exit=AlgorithmFailure('foo'),
            free_text_message='bar',
            rebase=DockerRebaseStrategy(
                frm='frm',
                next_train_tags=['tag1', 'tag2'],
                export_files=[]
            ))
        self.response2 = RunResponse(
            run_exit=AlgorithmFailure('bar'),
            free_text_message='Some text',
            rebase=DockerRebaseStrategy(
                frm='some remote Docker repository',
                next_train_tags=[],
                export_files=[
                    ModelFile('key1'),
                    ModelFile('key2'),
                    AlgorithmFile('key3')
                ]))

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
            actual=self.response1.as_dict())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'version': '1.0',
                'exit': {
                    'state': 'failure',
                    'reason': 'bar'
                },
                'free_text_message': 'Some text',
                'rebase': {
                    'export_files': [
                        {
                            'absolute_path': '/opt/pht_train/algorithm/key3',
                            'type': 'AlgorithmFile',
                            'display': 'AlgorithmFile'
                        },
                        {
                            'absolute_path': '/opt/pht_train/model/key1',
                            'type': 'ModelFile',
                            'display': 'ModelFile'
                        },
                        {
                            'absolute_path': '/opt/pht_train/model/key2',
                            'type': 'ModelFile',
                            'display': 'ModelFile'
                        }
                    ],
                    'next_train_tags': [],
                    'from': 'some remote Docker repository',
                    'type': 'docker',
                    'display': 'docker'
                },
                'type': 'RunResponse',
                'display': 'RunResponse'
            },
            actual=self.response2.as_dict())

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response1.type)

    def test_type_2(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response2.type)

    ################################################################################
    # Display
    ################################################################################
    def test_display_1(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response1.display)

    def test_display_2(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response2.display)

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
            actual=self.response1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={
                'version': '1.0',
                'exit': {
                    'state': 'failure',
                    'reason': 'bar'
                },
                'free_text_message': 'Some text',
                'rebase': {
                    'export_files': [
                        {
                            'absolute_path': '/opt/pht_train/algorithm/key3',
                            'type': 'AlgorithmFile', 'display': 'AlgorithmFile'
                        },
                        {
                            'absolute_path': '/opt/pht_train/model/key1',
                            'type': 'ModelFile',
                            'display': 'ModelFile'
                        },
                        {
                            'absolute_path': '/opt/pht_train/model/key2',
                            'type': 'ModelFile',
                            'display': 'ModelFile'
                        }
                    ],
                    'next_train_tags': [],
                    'from': 'some remote Docker repository',
                    'type': 'docker',
                    'display': 'docker'
                }
            },
            actual=self.response2.data)
