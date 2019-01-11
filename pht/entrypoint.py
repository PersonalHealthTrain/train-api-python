import abc
import argparse
from .train import Train
from .response import Response
from .station import StationRuntimeInfo

RESPONSE_UNDEFINED = 1
_choices = 'choices'
_dispatcher = 'dispatcher'
_run = 'run'
_print_summary = 'print_summary'
_list = 'list'


class Dispatcher(abc.ABC):

    @abc.abstractmethod
    def compute_response(self, run_info: StationRuntimeInfo, args) -> Response:
        pass

    def print_response(self, run_info: StationRuntimeInfo, args):
        response = self.compute_response(run_info, args)
        print(response.to_json_string(), flush=True)


class AlgorithmDispatcher(Dispatcher):
    def __init__(self, train: Train):
        self.train = train

    def compute_response(self, run_info: StationRuntimeInfo, args):
        if args.TOOL == _run:
            return self.train.run_algorithm(run_info)


class ModelDispatcher(Dispatcher):
    def __init__(self, train: Train):
        self.train = train

    def compute_response(self, run_info: StationRuntimeInfo, args):
        if args.TOOL == _print_summary:
            return self.train.print_model_summary(run_info)


class RequirementsDispatcher(Dispatcher):
    def __init__(self, train: Train):
        self.train = train

    def compute_response(self, run_info: StationRuntimeInfo, args) -> Response:
        if args.TOOL == _list;
            return self.train.


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

    # The subparsers
    _subparsers = {
        'algorithm': {
            _choices: [_run],
            _dispatcher: AlgorithmDispatcher(train)
        },
        'model': {
            _choices: [_print_summary],
            _dispatcher: ModelDispatcher(train)
        },
        'requirements': {
            _choices: [_list],

        }
    }
    for (name, details) in _subparsers.items():
        subparser = subparsers.add_parser(name)
        subparser.add_argument(
            TOOL, choices=details[_choices]
        )
        subparser.set_defaults(dispatcher=details[_dispatcher])

    args = parser.parse_args()
    run_info = StationRuntimeInfo(
        station_id=args.station_id,
        track_info=args.track_info,
        user_data=args.user_data
    )

    args.dispatcher.print_response(run_info, args)


    #
    # parser_requirements = subparsers.add_parser('requirements')
    # parser_requirements.add_argument(
    #     TOOL, choices=['list'])
    # parser_requirements.add_argument(
    #     '--check', required=False, action='store_true', help='Whether the train should check that the requirements are met')




    # Perform action depending on the selected tool and print the result
