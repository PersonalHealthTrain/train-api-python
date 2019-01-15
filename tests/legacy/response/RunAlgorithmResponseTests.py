import unittest
from pht.internal.response import RunAlgorithmResponse, AlgorithmExitState
from pht.internal.rebase import DockerRebaseStrategy


class RunAlgorithmResponseTests(unittest.TestCase):

    def test_run_algorithm_1(self):
        response = RunAlgorithmResponse(
            AlgorithmExitState.SUCCESS,
            'tests',
            'foobar',
            DockerRebaseStrategy('personalhealthtrain/train_test:base'), []).to_json_string()
        message = '{"type": "RunAlgorithmResponse",' \
                  ' "state": "SUCCESS",' \
                  ' "message": "tests",' \
                  ' "next_train_tag": "foobar",' \
                  ' "rebase": {"type": "docker",' \
                  ' "from": "personalhealthtrain/train_test:base"}, "export_files": []}'
        self.assertEqual(response, message)

    def test_run_algorithm_2(self):
        response = RunAlgorithmResponse(
            AlgorithmExitState.FAILURE,
            'tests',
            'foobar',
            DockerRebaseStrategy('personalhealthtrain/train_test:base'), []).to_json_string()
        message = '{"type": "RunAlgorithmResponse",' \
                  ' "state": "FAILURE",' \
                  ' "message": "tests",' \
                  ' "next_train_tag": "foobar",' \
                  ' "rebase": {"type": "docker",' \
                  ' "from": "personalhealthtrain/train_test:base"}, "export_files": []}'
        self.assertEqual(response, message)

