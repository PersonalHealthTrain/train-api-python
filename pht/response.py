"""
Defines the responses classes of trains according to the schema definition

@author Lukas Zimmermann
"""
import json
from .util import without_none_values
import abc
from typing import List

# DICT Keys
MESSAGE = 'message'
SUCCESS = 'success'
UNMET = 'unmet'
NEXT_TRAIN_TAG = 'nextTrainTag'
REQUIREMENTS = 'requirements'


class Response(abc.ABC):

    @abc.abstractmethod
    def as_json(self):
        pass

    @staticmethod
    def fields_to_json(d):
        return json.dumps(without_none_values(d))


class RunAlgorithmResponse(Response):

    def __init__(self, success: bool, next_train_tag: str, message: str = None):
        self.success = success
        self.next_train_tag = next_train_tag
        self.message = message

    def as_json(self):
        return Response.fields_to_json({

            SUCCESS: self.success,
            NEXT_TRAIN_TAG: self.next_train_tag,
            MESSAGE: self.message
        })


class ListRequirementsResponse(Response):
    def __init__(self, requirements: List[str]):
        self.requirements = requirements

    def as_json(self):
        return Response.fields_to_json({
            REQUIREMENTS: self.requirements
        })


class CheckRequirementsResponse(Response):
    def __init__(self, unmet: List[str], message: str = None):
        self.unmet = unmet
        self.message = message

    def as_json(self):
        return Response.fields_to_json({
            UNMET: self.unmet,
            MESSAGE: self.message
        })
