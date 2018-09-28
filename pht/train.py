from abc import abstractmethod, ABC
import argparse
import enum
from .response import RunAlgorithmResponse
from .response import CheckRequirementsResponse
from .response import ListRequirementsResponse
from .response import Response
from .exit_codes import RESPONSE_UNDEFINED
import sys


class TrainMode(enum.Enum):
    """
    Represents potential train modes. Currently, only immediate is supported
    """
    IMMEDIATE = 'IMMEDIATE'


class RunInfo:
    """
    Represents information on the station that will be passed on runtime.
    Currently, these information encompass the station_id and the train mode.
    """
    def __init__(self, station_id: int, train_mode: TrainMode):
        self.station_id = station_id
        self.train_mode = train_mode


class Train(ABC):
    """
    Implements the API of a train
    """
    @abstractmethod
    def run_algorithm(self, run_info: RunInfo) -> RunAlgorithmResponse:
        pass

    @abstractmethod
    def print_summary(self, run_info: RunInfo) -> str:
        pass

    @abstractmethod
    def check_requirements(self, run_info: RunInfo) -> CheckRequirementsResponse:
        pass

    @abstractmethod
    def list_requirements(self, run_info: RunInfo) -> ListRequirementsResponse:
        pass


def cmd_for_train(train: Train):

    # CMDs
    tool_run_algorithm = "run_algorithm"
    tool_print_summary = "print_summary"
    tool_check_requirements = "check_requirements"
    tool_list_requirements = "list_requirements"

    parser = argparse.ArgumentParser()
    parser.add_argument('tool',
                        choices=[
                            tool_run_algorithm,
                            tool_print_summary,
                            tool_check_requirements,
                            tool_list_requirements
                        ],
                        help="The subroutine that the train will perform once it is run")
    parser.add_argument('--stationid', type=int, required=True)
    parser.add_argument('--mode', type=str, default='immediate')
    args = parser.parse_args()

    # Determine the run information from the command line arguments
    run_info = RunInfo(
        station_id=args.stationid,
        train_mode=TrainMode[args.mode.upper()])

    # Perform action depending on the selected tool and print the result
    tool = args.tool
    response: Response = None
    if tool == tool_run_algorithm:
        response = train.run_algorithm(run_info).as_json()
    elif tool == tool_print_summary:
        response = train.print_summary(run_info)
    elif tool == tool_check_requirements:
        response = train.check_requirements(run_info).as_json()
    elif tool == tool_list_requirements:
        response = train.list_requirements(run_info).as_json()

    # Exit with 1 if the train does
    if response is None:
        sys.exit(RESPONSE_UNDEFINED)

    # The response is by default print to stdout
    print(response)

