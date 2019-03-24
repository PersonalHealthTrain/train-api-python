import abc
import json
import os
from typing import Optional, Union
from tests.base import BaseTest
from unittest.mock import patch
from pht.internal.response.describe.requirement import Require, Forbid, Any
from pht.internal.train.SimpleDockerTrain import SimpleDockerTrain
from pht.internal.train.StationRuntimeInfo import StationRuntimeInfo
from pht.internal.response.describe.requirement.builder import ConjunctionBuilder
from pht.internal.response.describe.property.environment_variable import enum_by_name, url_by_name, bind_mount_by_name
from pht.internal.response.run.exit.RunExit import AlgorithmSuccessRunExit, AlgorithmFailureRunExit, AlgorithmApplicationRunExit
from pht.internal.response.describe.property.environment_variable.BindMountEnvironmentVariableProperty import MountType


class DescribeOnlyTrain(SimpleDockerTrain):
    def __init__(self):
        super().__init__('test_train', '1.0', 'personalhealthtrain/rebase', ['foo'])

    def model_summary(self) -> str:
        return 'foo'

    def run_algorithm(self, info: StationRuntimeInfo, log):
        pass

    @abc.abstractmethod
    def requirements(self) -> Optional[ConjunctionBuilder]:
        pass


##################################
#  Trains only using URLs
##################################
class _TestTrain1(SimpleDockerTrain):
    def __init__(self):
        super().__init__('test_train', '1.0', 'personalhealthtrain/base', ['train-tag'])

    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO'))

    def model_summary(self) -> str:
        return 'foo'

    def run_algorithm(self, info: StationRuntimeInfo, log):
        log.set_exit_state(AlgorithmSuccessRunExit('Execution ran successfully'))
        log.set_free_text_message('test')


class _TestTrain2(SimpleDockerTrain):

    def __init__(self):
        super().__init__('test_train', '1.0', 'personalhealthtrain/base:base', ['2.7.15-slim-jessie'])

    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Require(url_by_name('BAR'))

    def model_summary(self) -> str:
        return 'foo'

    def run_algorithm(self, info: StationRuntimeInfo, log):
        log.set_free_text_message('This is arbitrary free text')
        log.set_exit_state(AlgorithmFailureRunExit('Execution of the algorithm failed'))


class _TestTrain3(SimpleDockerTrain):
    def __init__(self):
        super().__init__('test_train', '1.0', 'personalhealthtrain/base:base', ['latest'])

    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')))

    def model_summary(self) -> str:
        return 'foo'

    def run_algorithm(self, info: StationRuntimeInfo, log):
        log.set_exit_state(AlgorithmApplicationRunExit('Application specific error, not success, but also not failure'))
        log.set_free_text_message('This is arbitrary free text')


class _TestTrain4(DescribeOnlyTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM')))


class _TestTrain5(DescribeOnlyTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM'))) & Require(url_by_name('FOO')) & Forbid(url_by_name('CAT'))


class _TestTrain6(DescribeOnlyTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM'))) & Any(Require(url_by_name('FOO')) | Forbid(url_by_name('CAT')))


class _TestTrain7(DescribeOnlyTrain):
    def __init__(self):
        super().__init__()
        self.source1 = url_by_name('DATA_SOURCE_A')
        self.source2 = url_by_name('DATA_SOURCE_B')
        self.source3 = url_by_name('DATA_SOURCE_C')
        self.forbidden = url_by_name('FORBIDDEN')

    def requirements(self):
        return Require(self.source1) & Any(Require(self.source2) | Require(self.source3)) & Forbid(self.forbidden)


# Any with only one argument is not allowd
class _TestTrain8(DescribeOnlyTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Require(url_by_name('FOO')))


# Argument to Literal is not a valid property
class _TestTrain9(DescribeOnlyTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Forbid(url_by_name('FOO')) & Forbid('foo')


class _TestTrain10(DescribeOnlyTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Forbid(url_by_name('BAZ')) & Forbid(url_by_name('BAM'))


class _TestTrain11(DescribeOnlyTrain):
    def requirements(self):
        pass


######################################################################################
#  Trains also using enums
######################################################################################
class _TestTrain12(DescribeOnlyTrain):
    def requirements(self):
        return Require(enum_by_name('FOO', choices=['VALUE1', 'VALUE2']))


class _TestTrain13(DescribeOnlyTrain):
    def requirements(self):
        return Require(enum_by_name('FOO', choices=['VALUE1', 'VALUE2']))


class _TestTrain14(DescribeOnlyTrain):
    def requirements(self):
        return Require(enum_by_name('FOO', choices=['VALUE1', 'VALUE2']))


class _TestTrain15(DescribeOnlyTrain):
    def requirements(self):
        return Require(bind_mount_by_name('FOO', MountType.FILE))


class _TestTrain16(DescribeOnlyTrain):
    def requirements(self):
        return Require(bind_mount_by_name('FOO', MountType.DIRECTORY))


######################################################################################
#  Trains that operate on a File System mount
######################################################################################
class _TestTrain17(SimpleDockerTrain):
    def __init__(self):
        super().__init__('test_train', '1.0', 'personalhealthtrain/base:base', ['2.7.15-slim-jessie'])

    def requirements(self):
        return Require(
            bind_mount_by_name(
                'DATA_FILE_LOCATION',
                mount_type=MountType.FILE,
                description='The location for the data files of use case X'))

    # We do not expect the model file to be exported, since it does not have any content
    def run_algorithm(self, info: StationRuntimeInfo, log):
        self.model_file('fo')

    def model_summary(self) -> Union[str, dict, list]:
        return 'model summary'


class _TestTrain18(SimpleDockerTrain):
    def __init__(self):
        super().__init__('test_train', '1.0', 'personalhealthtrain/base:base', ['2.7.15-slim-jessie', 'latest'])

    def requirements(self):
        return Require(
            bind_mount_by_name(
                'DATA_DIRECTORY_LOCATION',
                mount_type=MountType.DIRECTORY,
                description='The location for the data files of use case X'))

    def model_summary(self) -> Union[str, dict, list]:
        return {
            'param1': 719,
            'param2': 1
        }

    def run_algorithm(self, info: StationRuntimeInfo, log):
        self.model_file('key').write('Some value')


station_runtime_info = StationRuntimeInfo(1)


def _load_json(name: str) -> dict:
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', name)
    with open(file_path, 'r') as f:
        text = ' '.join(f.readlines())
    return json.loads(text)


class SimpleTrainTests(BaseTest):

    def perform_test(self, train_response, file: str):
        self.maxDiff = None
        self.checkExpect(
            expect=_load_json(file),
            actual=train_response.as_simple_dict())


class SimpleTrainDescribeTests(SimpleTrainTests):

    def describe_test(self, train: SimpleDockerTrain, file: str):
        self.perform_test(train.describe(station_runtime_info), file)

    def test_describe_1(self):
        self.describe_test(_TestTrain1(), 'train1_describe.json')

    def test_describe_2(self):
        self.describe_test(_TestTrain2(), 'train2_describe.json')

    def test_describe_3(self):
        self.describe_test(_TestTrain3(), 'train3_describe.json')

    def test_describe_4(self):
        self.describe_test(_TestTrain4(), 'train4_describe.json')

    def test_describe_5(self):
        self.describe_test(_TestTrain5(), 'train5_describe.json')

    def test_describe_6(self):
        self.describe_test(_TestTrain6(), 'train6_describe.json')

    def test_describe_7(self):
        self.describe_test(_TestTrain7(), 'train7_describe.json')

    # TestTrain cannot describe, because the implementation of requirements is incorrect
    def test_describe_8(self):
        with self.assertRaises(ValueError):
            _TestTrain8().describe(station_runtime_info).as_json_string()

    # Argument to literal is not a valid property
    def test_describe_9(self):
        with self.assertRaises(ValueError):
            _TestTrain9().describe(station_runtime_info).as_json_string()

    def test_describe_10(self):
        self.describe_test(_TestTrain10(), 'train10_describe.json')

    def test_describe_11(self):
        self.describe_test(_TestTrain11(), 'train11_describe.json')

    # test enum, do not set the env var in the environment
    def test_describe_12(self):
        self.describe_test(_TestTrain12(), 'train12_describe.json')

    # test enum, set the environment variable, but to a wrong value
    def test_describe_13(self):
        with patch.dict('os.environ', {'FOO': 'VALUE3'}):
            self.describe_test(_TestTrain13(), 'train13_describe.json')

    # test enum, set the environment variable to an allowed value
    def test_describe_14(self):
        with patch.dict('os.environ', {'FOO': 'VALUE2'}):
            self.describe_test(_TestTrain14(), 'train14_describe.json')

    # test bind_mount, environment variable not present
    def test_describe_15(self):
        self.describe_test(_TestTrain15(), 'train15_describe.json')

    def test_describe_16(self):
        self.describe_test(_TestTrain16(), 'train16_describe.json')

    def test_describe_17(self):
        self.describe_test(_TestTrain17(), 'train17_describe.json')

    def test_describe_18(self):
        self.describe_test(_TestTrain18(), 'train18_describe.json')


class SimpleTrainRunTests(SimpleTrainTests):

    def run_test(self, train: SimpleDockerTrain, file: str):
        self.perform_test(train.run(station_runtime_info), file)

    def test_run_1(self):
        self.run_test(_TestTrain1(), 'train1_run.json')

    def test_run_2(self):
        self.run_test(_TestTrain2(), 'train2_run.json')

    def test_run_3(self):
        self.run_test(_TestTrain3(), 'train3_run.json')

    def test_run_17(self):
        self.run_test(_TestTrain17(), 'train17_run.json')

    def test_run_18(self):
        self.run_test(_TestTrain18(), 'train18_run.json')
