from tests.base import BaseTest
from pht.internal.train.StationRuntimeInfo import StationRuntimeInfo


class StationRuntimeInfoTests(BaseTest):

    def setUp(self):
        self.station1 = StationRuntimeInfo(1)
        self.station2 = StationRuntimeInfo(2, track_info='foo')
        self.station3 = StationRuntimeInfo(3, user_data='bar')
        self.station4 = StationRuntimeInfo(4, track_info='foo', user_data='bar')

    #####################################################################################
    # Value error
    #####################################################################################
    def test_type_error_1(self):
        self.assertValueError(lambda: StationRuntimeInfo(None))

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
        self.assertCopiesAreEqual(self.station1)

    def test_copy_2(self):
        self.assertCopiesAreEqual(self.station2)

    def test_copy_3(self):
        self.assertCopiesAreEqual(self.station3)

    def test_copy_4(self):
        self.assertCopiesAreEqual(self.station4)
