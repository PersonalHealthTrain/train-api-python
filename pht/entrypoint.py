"""
Contains functions to create the 'entrypoint' of the frontend program that executes the train.

If the train is run inside a container, a call of one of these functions should be the entrypoint of the container.
"""
import argparse
import sys
from pht.internal.train import AbstractTrain, StationRuntimeInfo


def cli_for_train(train: AbstractTrain):
    """
    Creates a command-line interface for the provided abstract train.
    :param train: The abstract train for which the CLI should be created
    """
    _describe = 'describe'
    _run = 'run'

    def _fprint(msg: str):
        print(msg, flush=True)

    def _exit_unsupported_command():
        sys.exit(1)

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
    tool = args.TOOL
    if tool == _run:
        _fprint(train.run(info).to_json_string())
    elif tool == _describe:
        _fprint(train.describe(info).to_json_string())
    else:
        _exit_unsupported_command()
