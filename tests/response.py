import unittest
from pht.response.exit_state import SUCCESS
from pht.response import RunResponse
from pht.rebase import DockerRebaseStrategy


class RunResponseTests(unittest.TestCase):

    def test_run_response_1(self):
        response = RunResponse(
            state=SUCCESS,
            message='test',
            next_train_tag='train_tag',
            rebase=DockerRebaseStrategy(frm='personalhealthtrain/base'),
            export_files=[]
        )
        print(response.to_json_string())
