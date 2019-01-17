import unittest
from pht.response.exit_state import SUCCESS, FAILURE
from pht.response import RunResponse
from pht.rebase import DockerRebaseStrategy


class RunResponseTests(unittest.TestCase):

    def test_run_response_1(self):
        response = RunResponse(
            state=SUCCESS,
            free_text_message='test',
            next_train_tag='train-tag',
            rebase=DockerRebaseStrategy(frm='personalhealthtrain/base'),
            export_files=[]
        )
        text = response.to_json_string()
        self.assertEqual('{"state": "success", "message": "test", "next_train_tag": "train-tag", "rebase": {"from": "personalhealthtrain/base", "type": "docker", "display": "docker"}, "export_files": []}', text)

    def test_run_response_2(self):
        response = RunResponse(
            state=FAILURE,
            free_text_message='This is arbitrary free text',
            next_train_tag='2.7.15-slim-jessie',
            rebase=DockerRebaseStrategy(frm='personalhealthtrain/base:base'),
            export_files=[]
        )
        text = response.to_json_string()
        self.assertEqual('{"state": "failure", "message": "This is arbitrary free text", "next_train_tag": "2.7.15-slim-jessie", "rebase": {"from": "personalhealthtrain/base:base", "type": "docker", "display": "docker"}, "export_files": []}', text)
