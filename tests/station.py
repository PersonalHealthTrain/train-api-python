import unittest
from pht.station import StationRuntimeInfo


class StationTests(unittest.TestCase):

    def test_valid_station_runtime_info(self):
        StationRuntimeInfo(1, 'foo', 'bar')
        StationRuntimeInfo(2)
        StationRuntimeInfo(3, track_info=None, user_data='foo')
        StationRuntimeInfo(4, track_info='bar', user_data=None)

    def test_none_as_station_id_is_not_allowed(self):
        with self.assertRaises(ValueError):
            StationRuntimeInfo(None)
