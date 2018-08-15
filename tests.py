from testcontainers.core.generic import GenericContainer
from pht.station import StationClient
import time
import tempfile
import os

# Environment variables that need to be set for the test container
# "PHT_DATA_STORAGE_FILENAME"
# "PHT_DATA_STORAGE_NAME"
PORT = 5000
STATION_NAME = "station"
station_container_name = "personalhealthtrain/test-data-storage-service:latest"
station_container = GenericContainer(station_container_name)\
    .with_exposed_ports(PORT)\
    .with_env('PHT_DATA_STORAGE_FILENAME', 'processed.cleveland.data')\
    .with_env("PHT_DATA_STORAGE_NAME", STATION_NAME)


def station_client_of(station):
    time.sleep(2)
    host = station.get_container_host_ip()
    port = station.get_exposed_port(PORT)
    return StationClient(host + ':' + port)


def count_lines_in_file(filename):
    with open(filename, 'r') as f:
        return len(list(f))


def test_station_client_1():
    with station_container as station:
        client = station_client_of(station)
        assert client.request_name() == STATION_NAME


def test_station_client_2():
    with station_container as station:
        client = station_client_of(station)
        output_file = tempfile.mkstemp()[1]
        client.request_data(output_file)
        assert count_lines_in_file(output_file) == 303
        os.remove(output_file)
