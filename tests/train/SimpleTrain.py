import unittest

from pht.internal import ConjunctionBuilder
from pht.train import SimpleTrain
from pht.requirement import Require, Forbid, Any, url_by_name
from pht.response import RunResponse


class _Base(SimpleTrain):

    def model_summary(self) -> str:
        return 'foo'

    def run(self) -> RunResponse:
        pass


class _TestTrain1(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO'))


class _TestTrain2(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Require(url_by_name('BAR'))


class _TestTrain3(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO')) & Any(Forbid(url_by_name('BAZ')) | Require(url_by_name('BAR')))


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

    def run(self) -> RunResponse:
        pass


class SimpleTrainTests(unittest.TestCase):

    def test_1(self):
        text = _TestTrain1().describe().to_json_string()
        self.assertEqual('{"properties": [{"id": 1, "data": {"target": "http://schema.org/URL", "name": "FOO", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}], "formula": [{"id": 1, "data": {"value": [[1]], "type": "https://www.wikidata.org/wiki/Q846564", "display": "ConjunctiveNormalForm"}}], "model": {"summary": "foo"}, "algorithm": {"requirement": {"value": 1, "type": "FormulaAlgorithmRequirement", "display": "FormulaAlgorithmRequirement"}}}', text)

    def test_2(self):
        text = _TestTrain2().describe().to_json_string()
        self.assertEqual('{"properties": [{"id": 1, "data": {"target": "http://schema.org/URL", "name": "FOO", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 2, "data": {"target": "http://schema.org/URL", "name": "BAR", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}], "formula": [{"id": 1, "data": {"value": [[1], [2]], "type": "https://www.wikidata.org/wiki/Q846564", "display": "ConjunctiveNormalForm"}}], "model": {"summary": "foo"}, "algorithm": {"requirement": {"value": 1, "type": "FormulaAlgorithmRequirement", "display": "FormulaAlgorithmRequirement"}}}', text)

    def test_3(self):
        text = _TestTrain3().describe().to_json_string()
        self.assertEqual('{"properties": [{"id": 1, "data": {"target": "http://schema.org/URL", "name": "FOO", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 2, "data": {"target": "http://schema.org/URL", "name": "BAZ", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 3, "data": {"target": "http://schema.org/URL", "name": "BAR", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}], "formula": [{"id": 1, "data": {"value": [[1], [3, -2]], "type": "https://www.wikidata.org/wiki/Q846564", "display": "ConjunctiveNormalForm"}}], "model": {"summary": "foo"}, "algorithm": {"requirement": {"value": 1, "type": "FormulaAlgorithmRequirement", "display": "FormulaAlgorithmRequirement"}}}', text)

    def test_4(self):
        text = _TestTrain4().describe().to_json_string()
        self.assertEqual('{"properties": [{"id": 1, "data": {"target": "http://schema.org/URL", "name": "BAZ", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 2, "data": {"target": "http://schema.org/URL", "name": "BAR", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 3, "data": {"target": "http://schema.org/URL", "name": "BAM", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}], "formula": [{"id": 1, "data": {"value": [[2, -3, -1]], "type": "https://www.wikidata.org/wiki/Q846564", "display": "ConjunctiveNormalForm"}}], "model": {"summary": "foo"}, "algorithm": {"requirement": {"value": 1, "type": "FormulaAlgorithmRequirement", "display": "FormulaAlgorithmRequirement"}}}', text)

    def test_5(self):
        text = _TestTrain5().describe().to_json_string()
        self.assertEqual('{"properties": [{"id": 1, "data": {"target": "http://schema.org/URL", "name": "BAZ", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 2, "data": {"target": "http://schema.org/URL", "name": "BAR", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 3, "data": {"target": "http://schema.org/URL", "name": "BAM", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 4, "data": {"target": "http://schema.org/URL", "name": "FOO", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 5, "data": {"target": "http://schema.org/URL", "name": "CAT", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}], "formula": [{"id": 1, "data": {"value": [[-5], [2, -3, -1], [4]], "type": "https://www.wikidata.org/wiki/Q846564", "display": "ConjunctiveNormalForm"}}], "model": {"summary": "foo"}, "algorithm": {"requirement": {"value": 1, "type": "FormulaAlgorithmRequirement", "display": "FormulaAlgorithmRequirement"}}}', text)

    def test_6(self):
        text = _TestTrain6().describe().to_json_string()
        self.assertEqual('{"properties": [{"id": 1, "data": {"target": "http://schema.org/URL", "name": "BAZ", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 2, "data": {"target": "http://schema.org/URL", "name": "BAR", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 3, "data": {"target": "http://schema.org/URL", "name": "BAM", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 4, "data": {"target": "http://schema.org/URL", "name": "FOO", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 5, "data": {"target": "http://schema.org/URL", "name": "CAT", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}], "formula": [{"id": 1, "data": {"value": [[-5, 4], [2, -3, -1]], "type": "https://www.wikidata.org/wiki/Q846564", "display": "ConjunctiveNormalForm"}}], "model": {"summary": "foo"}, "algorithm": {"requirement": {"value": 1, "type": "FormulaAlgorithmRequirement", "display": "FormulaAlgorithmRequirement"}}}', text)

    def test_7(self):
        text = _TestTrain7().describe().to_json_string()
        self.assertEqual('{"properties": [{"id": 1, "data": {"target": "http://schema.org/URL", "name": "DATA_SOURCE_A", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 2, "data": {"target": "http://schema.org/URL", "name": "DATA_SOURCE_B", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 3, "data": {"target": "http://schema.org/URL", "name": "DATA_SOURCE_C", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}, {"id": 4, "data": {"target": "http://schema.org/URL", "name": "FORBIDDEN", "check": false, "type": "http://www.wikidata.org/entity/Q400857", "display": "environmentVariable"}}], "formula": [{"id": 1, "data": {"value": [[-4], [1], [2, 3]], "type": "https://www.wikidata.org/wiki/Q846564", "display": "ConjunctiveNormalForm"}}], "model": {"summary": "foo"}, "algorithm": {"requirement": {"value": 1, "type": "FormulaAlgorithmRequirement", "display": "FormulaAlgorithmRequirement"}}}', text)
