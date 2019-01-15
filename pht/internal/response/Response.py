"""
Defines the responses classes of trains according to the schema definition

@author Lukas Zimmermann
"""
from abc import ABC, abstractmethod
import json


class Response(ABC):

    @property
    @abstractmethod
    def type(self) -> str:
        """
        The Type of the Response. Generally, this should be the name of the implementing Python class.
        :return:
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Represents the Response as dictionary
        :return: The dict-representation of the Response
        """
        pass

    def to_json_string(self):
        return json.dumps(self.to_dict())
