import argparse
from ..train import Train
from pht.station import StationRuntimeInfo


_run = 'run'


def _algorithm(train: Train):
    def func(args):
        print(args)
        # Determine the run information from the command line arguments
        run_info = StationRuntimeInfo(
            station_id=args.station_id,
            track_info=args.track_info,
            user_data=args.user_data
        )
        if args.TOOL == _run:
            print(train.run_algorithm(run_info).to_json_string())
    return func


def cmd_for_train(train: Train):
    TOOL = 'TOOL'

    parser = argparse.ArgumentParser(description='Command-line interface for running a train')
    parser.add_argument(
        '--station-id', type=int, required=True, help='The Station Id where the train is run at')
    parser.add_argument(
        '--track-info', type=str, required=False, help='Info on the Track that the Train is currently running on')
    parser.add_argument(
        '--user-data', type=str, required=False, help='Custom User data')
    subparsers = parser.add_subparsers()

    # Algorithm subparser
    parser_algorithm = subparsers.add_parser('algorithm')
    parser_algorithm.add_argument(
        TOOL, choices=[_run])
    parser_algorithm.set_defaults(func=_algorithm(train))

    args = parser.parse_args()
    args.func(args)


    # parser_model = subparsers.add_parser('model')
    # parser_model.add_argument(
    #     TOOL, choices=['print_summary'])
    #
    # parser_requirements = subparsers.add_parser('requirements')
    # parser_requirements.add_argument(
    #     TOOL, choices=['list'])
    # parser_requirements.add_argument(
    #     '--check', required=False, action='store_true', help='Whether the train should check that the requirements are met')




    # Perform action depending on the selected tool and print the result
