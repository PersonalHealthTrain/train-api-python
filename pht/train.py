from abc import abstractmethod, ABC
import argparse


class Train(ABC):
    """
    Implements the API of a train
    """

    def __init__(self):
        pass

    @abstractmethod
    def run_algorithm(self):
        pass

    @abstractmethod
    def print_summary(self):
        pass

    @abstractmethod
    def print_next_departure_id(self):
        pass

    @abstractmethod
    def check_requirements(self):
        pass


def cmd_for_train(train: Train):

    # CMDs
    tool_run_algorithm = "run_algorithm"
    tool_print_summary = "print_summary"
    tool_print_next_departure_id = "print_next_departure_id"
    tool_check_requirements = "check_requirements"

    parser = argparse.ArgumentParser()
    parser.add_argument('tool',
                        choices=[
                            tool_run_algorithm,
                            tool_print_summary,
                            tool_print_next_departure_id,
                            tool_check_requirements
                        ],
                        help="The subroutine that the train will perform once it is run")
    tool = parser.parse_args().tool

    if tool == tool_run_algorithm:
        train.run_algorithm()
    elif tool == tool_print_next_departure_id:
        train.print_next_departure_id()
    elif tool == tool_print_summary:
        train.print_summary()
    elif tool == tool_check_requirements:
        train.check_requirements()
