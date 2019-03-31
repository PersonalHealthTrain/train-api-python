"""
Contains functions to create the 'entrypoint' of the frontend script that executes the train.

If the train is run inside a container, a call of one of these functions should be the entrypoint of the container.
"""
import argparse
import sys
from pht.internal.train.TrainCommandInterface import TrainCommandInterface
from pht.internal.train.StationRuntimeInfo import StationRuntimeInfo


def cli_for_train(train: TrainCommandInterface):
    """
    Creates a command-line interface for the provided abstract train.
    :param train: The abstract train for which the CLI should be created
    """
    _describe = 'describe'
    _run = 'run'

    parser = argparse.ArgumentParser(description='Command-line interface for running a train')
    parser.add_argument('COMMAND', type=str, choices=[_describe, _run])
    parser.add_argument(
        '--station-id', type=int, required=True, help='The Station Id where the train is run at')
    parser.add_argument(
        '--track-info', type=str, required=False, help='Info on the Track that the Train is currently running on')
    parser.add_argument(
        '--user-data', type=str, required=False, help='Custom User data')

    args = parser.parse_args()
    info = StationRuntimeInfo(station_id=args.station_id, track_info=args.track_info, user_data=args.user_data)

    def _exit_unsupported_command():
        sys.exit(1)

    def _print_json_string_after(func):
        print(func(train).as_json_string(), flush=True)

    command = args.COMMAND
    if command == _run:
        _print_json_string_after(lambda x: x.run(info))
    elif command == _describe:
        _print_json_string_after(lambda x: x.describe(info))
    else:
        _exit_unsupported_command()
