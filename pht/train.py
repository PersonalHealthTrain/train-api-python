from abc import abstractmethod, ABC
import argparse
import enum
import json


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


class RunAlgorithmResult:
    """
    Represents the result of a run algorithm operation, which currently only contains the
    departure id.
    """
    def __init__(self, departure_tag: str):
        self.departure_tag = departure_tag

    def __repr__(self):
        return json.dumps({'departure_tag': self.departure_tag})

    def __str__(self):
        return self.__repr__()


class Train(ABC):
    """
    Implements the API of a train
    """

    def __init__(self):
        pass

    @abstractmethod
    def run_algorithm(self, run_info) -> RunAlgorithmResult:
        pass

    @abstractmethod
    def print_summary(self, run_info):
        pass

    @abstractmethod
    def check_requirements(self, run_info):
        pass


class ImmediateTrain(Train):
    """
    Represents a train that is called for the train mode immediate
    """
    def __int__(self):
        pass

    @abstractmethod
    def execute(self, run_info):
        pass

    def run_algorithm(self, run_info) -> RunAlgorithmResult:
        """
        For the ImmediateTrain class, the departure id will be identical to the station id
        """
        self.execute(run_info)
        return RunAlgorithmResult(departure_tag=run_info.station_id)


def cmd_for_train(train: Train):

    # CMDs
    tool_run_algorithm = "run_algorithm"
    tool_print_summary = "print_summary"
    tool_check_requirements = "check_requirements"

    parser = argparse.ArgumentParser()
    parser.add_argument('tool',
                        choices=[
                            tool_run_algorithm,
                            tool_print_summary,
                            tool_check_requirements
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
    if tool == tool_run_algorithm:
        print(train.run_algorithm(run_info))
    elif tool == tool_print_summary:
        train.print_summary(run_info)
    elif tool == tool_check_requirements:
        train.check_requirements(run_info)

