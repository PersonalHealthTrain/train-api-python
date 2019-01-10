import unittest

from pht.station import StationRuntimeInfo
from .testtrain import TestTrain


class TrainTests(unittest.TestCase):

    def setUp(self):
        self.train = TestTrain()
        self.station_info = StationRuntimeInfo(1)

    def test_model_summary(self):
        self.assertEqual('foo', self.train.print_model_summary(self.station_info).content)
