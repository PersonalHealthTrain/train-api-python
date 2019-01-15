import unittest

from pht.internal import ConjunctionBuilder
from pht.train import SimpleTrain
from pht.requirement import Require, Forbid, Any, url_by_name


class _Base(SimpleTrain):

    def model_summary(self) -> str:
        return 'foo'


class TestSimpleTrain(_Base):
    def requirements(self) -> ConjunctionBuilder:
        return Require(url_by_name('FOO'))



class SimpleTrainTests(unittest.TestCase):

    def test_1(self):
        print(TestSimpleTrain().describe().to_json_string())
