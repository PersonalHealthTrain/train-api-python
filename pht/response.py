"""
Defines the responses classes of trains according to the schema definition

@author Lukas Zimmermann
"""
import json
from .util import without_none_values
import abc
from typing import List
import enum
import typing


class ResponseKey(enum.Enum):
    SUCCESS = 'success'
    UNMET = 'unmet'
    NEXT_TRAIN_TAG = 'nextTrainTag'
    REQUIREMENTS = 'requirements'
    CONTENT = 'content'
    MESSAGE = 'message'


ResponseDict = typing.Dict[ResponseKey, typing.Any]


class Response(abc.ABC):

    def as_json(self) -> str:

        # Remove all the None values from the response dict
        d = without_none_values(self.as_response_dict())

        # Replace the ResponseKeys by their String representation
        d = {key.value: value for key, value in d.items()}

        # Return as a proper JSON string
        return json.dumps(d)

    @abc.abstractmethod
    def as_response_dict(self) -> ResponseDict:
        pass


class RunAlgorithmResponse(Response):

    def __init__(self, success: bool, message: str, next_train_tag: str):
        self.success = success
        self.message = message
        self.next_train_tag = next_train_tag

    def as_response_dict(self) -> ResponseDict:
        return {
            ResponseKey.SUCCESS: self.success,
            ResponseKey.MESSAGE: self.message,
            ResponseKey.NEXT_TRAIN_TAG: self.next_train_tag
        }


class ListRequirementsResponse(Response):
    def __init__(self, requirements: List[str]):
        self.requirements = requirements

    def as_response_dict(self) -> ResponseDict:
        return {
            ResponseKey.REQUIREMENTS: self.requirements
        }


class CheckRequirementsResponse(Response):
    def __init__(self, unmet: List[str]):
        self.unmet = unmet

    def as_response_dict(self) -> ResponseDict:
        return {
            ResponseKey.UNMET: self.unmet,
        }


class PrintSummaryResponse(Response):
    def __init__(self, content: str):
        self.content = content

    def as_response_dict(self) -> ResponseDict:
        return {
            ResponseKey.CONTENT: self.content
        }
