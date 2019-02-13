import unittest
from typing import List
from unittest.mock import patch
import json
import os

from pht.internal import ConjunctionBuilder, StationRuntimeInfo
from pht.train import SimpleDockerTrain
from pht.internal.describe.requirement import Require, Forbid, Any
from pht.internal.describe.requirement.env import enum_by_name, url_by_name
from pht.internal.train.RunExit import AlgorithmApplication, AlgorithmFailure, AlgorithmSuccess


class NoopTrain(SimpleDockerTrain):

    def model_summary(self) -> str:
        return 'foo'

    def default_rebase_from(self) -> str:
        return 'personalhealthtrain/rebase'

    def default_next_train_tags(self) -> List[str]:
        return ['foo']

    def run_algorithm(self, info: StationRuntimeInfo, log):
        pass


##################################
#  Trains only using URLs
##################################
class _TestTrain1(SimpleDockerTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO'))

    def default_rebase_from(self):
        return 'personalhealthtrain/base'

    def default_next_train_tags(self) -> List[str]:
        return ['train-tag']

    def model_summary(self) -> str:
        return 'foo'

    def run_algorithm(self, info: StationRuntimeInfo, log):
        log.set_exit_state(AlgorithmSuccess('Execution ran successfully'))
        log.set_free_text_message('test')


class _TestTrain2(SimpleDockerTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Require(url_by_name('BAR'))

    def model_summary(self) -> str:
        return 'foo'

    def default_rebase_from(self) -> str:
        return 'personalhealthtrain/base:base'

    def default_next_train_tags(self) -> List[str]:
        return ['2.7.15-slim-jessie']

    def run_algorithm(self, info: StationRuntimeInfo, log):
        log.set_free_text_message('This is arbitrary free text')
        log.set_exit_state(AlgorithmFailure('Execution of the algorithm failed'))


class _TestTrain3(SimpleDockerTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')))

    def default_rebase_from(self) -> str:
        return 'personalhealthtrain/base:base'

    def default_next_train_tags(self) -> List[str]:
        return ['latest']

    def model_summary(self) -> str:
        return 'foo'

    def run_algorithm(self, info: StationRuntimeInfo, log):
        log.set_exit_state(AlgorithmApplication('Application specific error, not success, but also not failure'))
        log.set_free_text_message('This is arbitrary free text')


class _TestTrain4(NoopTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM')))  # & Require(url_by_name('FOO')) & Forbid(url_by_name('CAT'))


class _TestTrain5(NoopTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM'))) & Require(url_by_name('FOO')) & Forbid(url_by_name('CAT'))


class _TestTrain6(NoopTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM'))) & Any(Require(url_by_name('FOO')) | Forbid(url_by_name('CAT')))


class _TestTrain7(NoopTrain):
    def __init__(self):
        super().__init__()
        self.source1 = url_by_name('DATA_SOURCE_A')
        self.source2 = url_by_name('DATA_SOURCE_B')
        self.source3 = url_by_name('DATA_SOURCE_C')
        self.forbidden = url_by_name('FORBIDDEN')

    def requirements(self):
        return Require(self.source1) & Any(Require(self.source2) | Require(self.source3)) & Forbid(self.forbidden)


# Any with only one argument is not allowd
class _TestTrain8(NoopTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Require(url_by_name('FOO')))


# Argument to Literal is not a valid property
class _TestTrain9(NoopTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Forbid(url_by_name('FOO')) & Forbid('foo')


class _TestTrain10(NoopTrain):
    def requirements(self) -> ConjunctionBuilder:
        return Forbid(url_by_name('BAZ')) & Forbid(url_by_name('BAM'))


class _TestTrain11(NoopTrain):
    def requirements(self):
        pass


##################################
#  Trains also using enums
##################################
class _TestTrain12(NoopTrain):
    def requirements(self):
        return Require(enum_by_name('FOO', choices=['VALUE1', 'VALUE2']))


class _TestTrain13(NoopTrain):
    def requirements(self):
        return Require(enum_by_name('FOO', choices=['VALUE1', 'VALUE2']))


class _TestTrain14(NoopTrain):
    def requirements(self):
        return Require(enum_by_name('FOO', choices=['VALUE1', 'VALUE2']))


info = StationRuntimeInfo(1)


def _load_json(name: str) -> dict:
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', name)
    with open(file_path, 'r') as f:
        text = ' '.join(f.readlines())
    return json.loads(text)


class SimpleTrainTests(unittest.TestCase):

    def perform_test(self, train_response, file: str):
        actual = train_response.as_dict()
        expect = _load_json(file)
        self.assertDictEqual(actual, expect)


class SimpleTrainDescribeTests(SimpleTrainTests):

    def describe_test(self, train: SimpleDockerTrain, file: str):
        self.perform_test(train.describe(info), file)

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
            _TestTrain8().describe(info).to_json_string()

    # Argument to literal is not a valid property
    def test_describe_9(self):
        with self.assertRaises(ValueError):
            _TestTrain9().describe(info).to_json_string()

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


class SimpleTrainRunTests(SimpleTrainTests):

    def run_test(self, train: SimpleDockerTrain, file: str):
        self.perform_test(train.run(info), file)

    def test_run_1(self):
        self.run_test(_TestTrain1(), 'train1_run.json')

    def test_run_2(self):
        self.run_test(_TestTrain2(), 'train2_run.json')

    def test_run_3(self):
        self.run_test(_TestTrain3(), 'train3_run.json')
