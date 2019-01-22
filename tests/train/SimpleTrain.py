import unittest
import json
import os

from pht.internal import ConjunctionBuilder, StationRuntimeInfo
from pht.train import SimpleTrain
from pht.requirement import Require, Forbid, Any, url_by_name
from pht.train.response import RunResponse
from pht.rebase import DockerRebaseStrategy
from pht.train.response.exit_state import APPLICATION, SUCCESS, FAILURE


class _Base(SimpleTrain):

    def model_summary(self) -> str:
        return 'foo'

    def run(self, info: StationRuntimeInfo) -> RunResponse:
        pass


class _TestTrain1(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO'))

    def run(self, info: StationRuntimeInfo) -> RunResponse:
        return RunResponse(
            state=SUCCESS,
            free_text_message='test',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/base',
                next_train_tag='train-tag',
                export_files=[]),
        )


class _TestTrain2(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Require(url_by_name('BAR'))

    def run(self, info: StationRuntimeInfo) -> RunResponse:
        return RunResponse(
            state=FAILURE,
            free_text_message='This is arbitrary free text',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/base:base',
                next_train_tag='2.7.15-slim-jessie',
                export_files=[]
            )
        )


class _TestTrain3(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')))

    def run(self, info: StationRuntimeInfo) -> RunResponse:
        return RunResponse(
            state=APPLICATION,
            free_text_message='This is arbitrary free text',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/base:base',
                next_train_tag='latest',
                export_files=[]
            )
        )


class _TestTrain4(_Base):
    def requirements(self) -> ConjunctionBuilder:

        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM')))  # & Require(url_by_name('FOO')) & Forbid(url_by_name('CAT'))


class _TestTrain5(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM'))) & Require(url_by_name('FOO')) & Forbid(url_by_name('CAT'))


class _TestTrain6(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')) | Forbid(url_by_name('BAM'))) & Any(Require(url_by_name('FOO')) | Forbid(url_by_name('CAT')))


class _TestTrain7(_Base):
    def __init__(self):
        self.source1 = url_by_name('DATA_SOURCE_A')
        self.source2 = url_by_name('DATA_SOURCE_B')
        self.source3 = url_by_name('DATA_SOURCE_C')
        self.forbidden = url_by_name('FORBIDDEN')

    def requirements(self):
        return Require(self.source1) & Any(Require(self.source2) | Require(self.source3)) & Forbid(self.forbidden)


# Any with only one argument is not allowd
class _TestTrain8(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Any(Require(url_by_name('FOO')))


# Argument to Literal is not a valid property
class _TestTrain9(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Forbid(url_by_name('FOO')) & Forbid('foo')


class _TestTrain10(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Forbid(url_by_name('BAZ')) & Forbid(url_by_name('BAM'))


info = StationRuntimeInfo(1)


def _load_json(name: str) -> dict:
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', name)
    with open(file_path, 'r') as f:
        text = ' '.join(f.readlines())
    return json.loads(text)


class SimpleTrainTests(unittest.TestCase):

    def perform_test(self, train_response, file: str):
        actual = train_response.dict()
        expect = _load_json(file)
        self.assertDictEqual(actual, expect)


class SimpleTrainDescribeTests(SimpleTrainTests):

    def describe_test(self, train: SimpleTrain, file: str):
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


class SimpleTrainRunTests(SimpleTrainTests):

    def run_test(self, train: SimpleTrain, file: str):
        self.perform_test(train.run(info), file)

    def test_run_1(self):
        self.run_test(_TestTrain1(), 'train1_run.json')

    def test_run_2(self):
        self.run_test(_TestTrain2(), 'train2_run.json')

    def test_run_3(self):
        self.run_test(_TestTrain3(), 'train3_run.json')
