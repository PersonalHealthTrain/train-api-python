from collections.abc import Hashable
from typing import Optional
from pht.internal.protocol.Copyable import Copyable
from pht.internal.util import require
from pht.internal.util.require import is_not_none


class StationRuntimeInfo(Copyable, Hashable):
    """
    Represents information on the station that will be passed on runtime.
    """
    def __init__(self, station_id: int, track_info: Optional[str] = None, user_data: Optional[str] = None):

        # Numeric Id of the station that executed the train (required)
        self.station_id = station_id
        require.for_value(self.station_id,
                          that=is_not_none,
                          error_if_not='Station ID was encountered to be None. This is not allowed.')

        # Optional Info about the track that the train is currently running on
        self.track_info = track_info

        # Custom User Data that
        self.user_data = user_data

    def __eq__(self, other):
        return other is self or \
               (isinstance(other, StationRuntimeInfo) and self.station_id == other.station_id and
                self.track_info == other.track_info and self.user_data == other.user_data)

    def __hash__(self):
        return hash((self.station_id, self.track_info, self.user_data))

    def copy(self):
        return StationRuntimeInfo(self.station_id, self.track_info, self.user_data)
