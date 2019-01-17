import argparse
import sys
from pht.internal import AbstractTrain, StationRuntimeInfo


def _fprint(msg: str):
    print(msg, flush=True)


def cmd_for_train(train: AbstractTrain):
    _describe = 'describe'
    _run = '_run'

    parser = argparse.ArgumentParser(description='Command-line interface for running a train')
    parser.add_argument('TOOL', type=str, choices=['describe', 'run'])
    parser.add_argument(
        '--station-id', type=int, required=True, help='The Station Id where the train is run at')
    parser.add_argument(
        '--track-info', type=str, required=False, help='Info on the Track that the Train is currently running on')
    parser.add_argument(
        '--user-data', type=str, required=False, help='Custom User data')

    args = parser.parse_args()
    info = StationRuntimeInfo(station_id=args.station_id , track_info=args.track_info, user_data=args.user_data)
    tool = args.TOOL
    if tool == _run:
        _fprint(train.run(info).to_json_string())
    elif tool == _describe:
        _fprint(train.describe(info).to_json_string())
    else:
        sys.exit(1)
