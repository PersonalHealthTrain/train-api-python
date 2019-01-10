import unittest
from unittest.mock import patch
from pht.entrypoint import cmd_for_train
from ..testtrain import TestTrain


class CmdForTrainTests(unittest.TestCase):


    def test_foo(self):
        with patch('sys.argv', ['TRAIN', '--station-id', '1', 'algorithm', 'run']):
            cmd_for_train(TestTrain())
