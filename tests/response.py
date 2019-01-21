import unittest
from pht.train.response.exit_state import SUCCESS, FAILURE
from pht.train.response import RunResponse
from pht.rebase import DockerRebaseStrategy


class RunResponseTests(unittest.TestCase):

    def test_run_response_1(self):
        response = RunResponse(
            state=SUCCESS,
            free_text_message='test',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/base',
                next_train_tag='train-tag',
                export_files=[]),
        )
        text = response.to_json_string()
        self.assertEqual('{"state": "success", "free_text_message": "test", "rebase": {"export_files": [], "next_train_tag": "train-tag", "from": "personalhealthtrain/base", "type": "docker", "display": "docker"}}', text)

    def test_run_response_2(self):
        response = RunResponse(
            state=FAILURE,
            free_text_message='This is arbitrary free text',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/base:base',
                next_train_tag='2.7.15-slim-jessie',
                export_files=[]
            )
        )
        text = response.to_json_string()
        self.assertEqual('{"state": "failure", "free_text_message": "This is arbitrary free text", "rebase": {"export_files": [], "next_train_tag": "2.7.15-slim-jessie", "from": "personalhealthtrain/base:base", "type": "docker", "display": "docker"}}', text)
