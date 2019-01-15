from typing import Optional
from pht.internal import fatal


class StationRuntimeInfo:
    """
    Represents information on the station that will be passed on runtime.
    """
    def __init__(self, station_id: int, track_info: Optional[str] = None, user_data: Optional[str] = None):

        # Numeric Id of the station that executed the train (required)
        self.station_id = station_id

        if self.station_id is None:
            raise ValueError(fatal('Station ID was encountered to be None. This is not allowed.'))

        # Optional Info about the track that the train is currently running on
        self.track_info = track_info

        # Custom User Data that
        self.user_data = user_data
