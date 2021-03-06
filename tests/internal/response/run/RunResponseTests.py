from tests.base import BaseTest
from pht.internal.response.run.exit.RunExit import AlgorithmFailureRunExit
from pht.internal.response.run.rebase.RebaseStrategy import DockerRebaseStrategy
from pht.internal.response.run.RunResponse import RunResponse
from pht.internal.train.cargo.ModelFile import ModelFile
from pht.internal.train.cargo.AlgorithmFile import AlgorithmFile


class RunResponseTests(BaseTest):

    def setUp(self):
        self.maxDiff = None
        self.response1 = RunResponse(
            run_exit=AlgorithmFailureRunExit('foo'),
            free_text_message='bar',
            rebase=DockerRebaseStrategy(
                frm='frm',
                next_train_tags=['tag1', 'tag2'],
                export_files=[]
            ))
        self.response2 = RunResponse(
            run_exit=AlgorithmFailureRunExit('bar'),
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
                'runResponseVersion': '1.0',
                'exit': {
                    "@type": ['AlgorithmFailureRunExit', 'RunExit'],
                    "@typeName": "AlgorithmFailureRunExit",
                    "@typeSystem": {
                        "name": "pythonclass",
                        "version": "1.0"
                    },
                    'state': 'failure',
                    'reason': 'foo'
                },
                'freeTextMessage': 'bar',
                'rebase': {
                    'exportFiles': [],
                    'nextTrainTags': ['tag1', 'tag2'],
                    'from': 'frm',
                    '@type': ['DockerRebaseStrategy', 'RebaseStrategy'],
                    '@typeName': 'DockerRebaseStrategy',
                    "@typeSystem": {
                        'name': 'pythonclass',
                        'version': '1.0'
                    },
                },
                '@type': ['RunResponse', 'TrainResponse'],
                '@typeName': 'RunResponse',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.response1.as_simple_mapping())

    def test_as_dict_2(self):
        self.checkExpect(
            expect={
                'runResponseVersion': '1.0',
                'exit': {
                    "@type": ["AlgorithmFailureRunExit", "RunExit"],
                    "@typeName": "AlgorithmFailureRunExit",
                    "@typeSystem": {
                        "name": "pythonclass",
                        "version": "1.0"
                    },
                    'state': 'failure',
                    'reason': 'bar'
                },
                'freeTextMessage': 'Some text',
                'rebase': {
                    'exportFiles': [
                        {
                            'absolutePhysicalPath': '/opt/pht_train/algorithm/key3',
                            '@type': ['AlgorithmFile', 'TrainFile'],
                            '@typeName': 'AlgorithmFile',
                            "@typeSystem": {
                                'name': 'pythonclass',
                                'version': '1.0'
                            },
                        },
                        {
                            'absolutePhysicalPath': '/opt/pht_train/model/key1',
                            '@type': ['ModelFile', 'TrainFile'],
                            '@typeName': 'ModelFile',
                            "@typeSystem": {
                                'name': 'pythonclass',
                                'version': '1.0'
                            },
                        },
                        {
                            'absolutePhysicalPath': '/opt/pht_train/model/key2',
                            '@type': ['ModelFile', 'TrainFile'],
                            '@typeName': 'ModelFile',
                            "@typeSystem": {
                                'name': 'pythonclass',
                                'version': '1.0'
                            },
                        }
                    ],
                    'nextTrainTags': [],
                    'from': 'some remote Docker repository',
                    '@type': ['DockerRebaseStrategy', 'RebaseStrategy'],
                    '@typeName': 'DockerRebaseStrategy',
                    "@typeSystem": {
                        'name': 'pythonclass',
                        'version': '1.0'
                    },
                },
                '@type': ['RunResponse', 'TrainResponse'],
                '@typeName': 'RunResponse',
                "@typeSystem": {
                    'name': 'pythonclass',
                    'version': '1.0'
                },
            },
            actual=self.response2.as_simple_mapping())

    ################################################################################
    # Type
    ################################################################################
    def test_type_1(self):
        self.checkExpect(
            expect=["RunResponse", "TrainResponse"],
            actual=self.response1.type)

    def test_type_2(self):
        self.checkExpect(
            expect=["RunResponse", "TrainResponse"],
            actual=self.response2.type)

    ################################################################################
    # Display
    ################################################################################
    def test_display_1(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response1.type_name)

    def test_display_2(self):
        self.checkExpect(
            expect='RunResponse',
            actual=self.response2.type_name)

    ################################################################################
    # Data
    ################################################################################
    def test_data_1(self):
        self.checkExpect(
            expect={
                'runResponseVersion': '1.0',
                'exit': {
                    "@type": ["AlgorithmFailureRunExit", "RunExit"],
                    "@typeName": "AlgorithmFailureRunExit",
                    "@typeSystem": {
                        "name": "pythonclass",
                        "version": "1.0"
                    },
                    'state': 'failure',
                    'reason': 'foo'
                },
                'freeTextMessage': 'bar',
                'rebase': {
                    'exportFiles': [],
                    'nextTrainTags': ['tag1', 'tag2'],
                    'from': 'frm',
                    '@type': ['DockerRebaseStrategy', 'RebaseStrategy'],
                    '@typeName': 'DockerRebaseStrategy',
                    "@typeSystem": {
                        'name': 'pythonclass',
                        'version': '1.0'
                    },
                }
            },
            actual=self.response1.data)

    def test_data_2(self):
        self.checkExpect(
            expect={
                'runResponseVersion': '1.0',
                'exit': {
                    '@type': ['AlgorithmFailureRunExit', 'RunExit'],
                    '@typeName': 'AlgorithmFailureRunExit',
                    "@typeSystem": {
                        "name": "pythonclass",
                        "version": "1.0"
                    },
                    'state': 'failure',
                    'reason': 'bar'
                },
                'freeTextMessage': 'Some text',
                'rebase': {
                    'exportFiles': [
                        {
                            'absolutePhysicalPath': '/opt/pht_train/algorithm/key3',
                            '@type': ['AlgorithmFile', 'TrainFile'],
                            '@typeName': 'AlgorithmFile',
                            "@typeSystem": {
                                'name': 'pythonclass',
                                'version': '1.0'
                            },
                        },
                        {
                            'absolutePhysicalPath': '/opt/pht_train/model/key1',
                            '@type': ['ModelFile', 'TrainFile'],
                            '@typeName': 'ModelFile',
                            "@typeSystem": {
                                'name': 'pythonclass',
                                'version': '1.0'
                            },
                        },
                        {
                            'absolutePhysicalPath': '/opt/pht_train/model/key2',
                            '@type': ['ModelFile', 'TrainFile'],
                            '@typeName': 'ModelFile',
                            "@typeSystem": {
                                'name': 'pythonclass',
                                'version': '1.0'
                            },
                        }
                    ],
                    'nextTrainTags': [],
                    'from': 'some remote Docker repository',
                    '@type': ['DockerRebaseStrategy', 'RebaseStrategy'],
                    '@typeName': 'DockerRebaseStrategy',
                    "@typeSystem": {
                        'name': 'pythonclass',
                        'version': '1.0'
                    },
                }
            },
            actual=self.response2.data)
