import unittest
from typing import List
from unittest.mock import patch
from pht.internal.entrypoint import cmd_for_train
from .testtrain import TestTrain


class CmdForTrainTests(unittest.TestCase):

    def train_command_line(self, line: List[str]):
        with patch('sys.argv', line):
            cmd_for_train(TestTrain())

    def test_algorithm_run(self):
        self.train_command_line(['TRAIN', '--station-id', '1', 'algorithm', 'run'])

    def test_model_print_summary(self):
        self.train_command_line(['TRAIN', '--station-id', '1', 'model', 'print_summary'])

