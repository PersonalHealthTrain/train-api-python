"""
Contains the StationRuntimeInfo class
"""
from collections.abc import Hashable
from typing import Optional
from pht.internal.protocol.DeepCopyable import DeepCopyable
from pht.internal.util import require


class StationRuntimeInfo(DeepCopyable, Hashable):
    """
    Represents information on the station that will be passed on runtime.
    """
    def __init__(self, station_id: int, track_info: Optional[str] = None, user_data: Optional[str] = None):
        self._station_id = station_id
        require.type_is_int(self._station_id)
        require.value_is_positive(self._station_id)

        self._track_info = track_info
        require.type_is_str_or_none(self._track_info)

        self._user_data = user_data
        require.type_is_str_or_none(self._user_data)

    @property
    def station_id(self) -> int:
        """The numerical i"""
        return self._station_id

    @property
    def track_info(self) -> Optional[str]:
        """The optional track info on which this train is executed"""
        return self._track_info

    @property
    def user_data(self):
        """The Optional User Data provided for the train"""
        return self._user_data

    def __eq__(self, other):
        return other is self or \
               (isinstance(other, StationRuntimeInfo) and self.station_id == other.station_id and
                self.track_info == other.track_info and self.user_data == other.user_data)

    def __hash__(self):
        return hash((self.station_id, self.track_info, self.user_data))

    def deepcopy(self):
        """Returns deep copy for this StationRuntimeInfo"""
        return StationRuntimeInfo(self.station_id, self.track_info, self.user_data)
