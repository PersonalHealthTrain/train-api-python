"""
Unit Tests for StationRuntimeInfo
"""
from tests.base import BaseTest
from pht.internal.train.StationRuntimeInfo import StationRuntimeInfo


class StationRuntimeInfoTests(BaseTest):

    def setUp(self):
        self.station1 = StationRuntimeInfo(1)
        self.station2 = StationRuntimeInfo(2, track_info='foo')
        self.station3 = StationRuntimeInfo(3, user_data='bar')
        self.station4 = StationRuntimeInfo(4, track_info='foo', user_data='bar')

    #####################################################################################
    # Station ID
    #####################################################################################
    def test_station_id_1(self):
        self.assertIsEqual(self.station1.station_id, 1)

    def test_station_id_unsassignable_1(self):
        with self.assertRaises(AttributeError):
            self.station1.station_id = 2

    def test_station_id_2(self):
        self.assertIsEqual(self.station2.station_id, 2)

    def test_station_id_unassignable_2(self):
        with self.assertRaises(AttributeError):
            self.station2.station_id = 3

    def test_station_id_3(self):
        self.assertIsEqual(self.station3.station_id, 3)

    def test_station_id_unassignable_3(self):
        with self.assertRaises(AttributeError):
            self.station3.station_id = 4

    def test_station_id_4(self):
        self.assertIsEqual(self.station4.station_id, 4)

    def test_station_id_unassignable_4(self):
        with self.assertRaises(AttributeError):
            self.station4.station_id = 5

    #####################################################################################
    # Track Info
    #####################################################################################
    def test_track_info_1(self):
        self.assertIsNone(self.station1.track_info)

    def test_track_info_unsassignable_1(self):
        with self.assertRaises(AttributeError):
            self.station1.track_info = 'foo'

    def test_track_info_2(self):
        self.assertIsEqual(self.station2.track_info, 'foo')

    def test_track_info_unassignable_2(self):
        with self.assertRaises(AttributeError):
            self.station2.track_info = 'bar'

    def test_track_info_3(self):
        self.assertIsNone(self.station3.track_info)

    def test_track_info_unassignable_3(self):
        with self.assertRaises(AttributeError):
            self.station3.track_info = 'baz'

    def test_track_info_4(self):
        self.assertIsEqual(self.station4.track_info, 'foo')

    def test_track_info_unassignable_4(self):
        with self.assertRaises(AttributeError):
            self.station4.track_info = 'bam'

    #####################################################################################
    # User Data
    #####################################################################################
    def test_user_data_1(self):
        self.assertIsNone(self.station1.track_info)

    def test_user_data_unsassignable_1(self):
        with self.assertRaises(AttributeError):
            self.station1.user_data= 'foo'

    def test_user_data_2(self):
        self.assertIsNone(self.station2.user_data)

    def test_user_data_unassignable_2(self):
        with self.assertRaises(AttributeError):
            self.station2.user_data = 'bar'

    def test_user_data_3(self):
        self.assertIsEqual(self.station3.user_data, 'bar')

    def test_user_data_unassignable_3(self):
        with self.assertRaises(AttributeError):
            self.station3.user_data = 'baz'

    def test_user_data_4(self):
        self.assertIsEqual(self.station4.user_data, 'bar')

    def test_user_data_unassignable_4(self):
        with self.assertRaises(AttributeError):
            self.station4.user_data = 'bam'


    #####################################################################################
    # Value error for wrong constructor invocation
    #####################################################################################
    def test_type_error_1(self):
        self.assertTypeError(lambda: StationRuntimeInfo(None))

    #####################################################################################
    # Value error for wrong constructor invocation
    #####################################################################################

    #####################################################################################
    # eq
    #####################################################################################
    def test_eq_1(self):
        self.assertIsEqual(self.station1, StationRuntimeInfo(1))

    def test_eq_2(self):
        self.assertIsEqual(self.station2, StationRuntimeInfo(2, track_info='foo'))

    def test_eq_3(self):
        self.assertIsEqual(self.station3, StationRuntimeInfo(3, user_data='bar'))

    def test_eq_4(self):
        self.assertIsEqual(self.station4, StationRuntimeInfo(4, track_info='foo', user_data='bar'))

    #####################################################################################
    # copy
    #####################################################################################
    def test_copy_1(self):
        self.assertCopiesAreEqualOf(self.station1)

    def test_copy_2(self):
        self.assertCopiesAreEqualOf(self.station2)

    def test_copy_3(self):
        self.assertCopiesAreEqualOf(self.station3)

    def test_copy_4(self):
        self.assertCopiesAreEqualOf(self.station4)
