"""
Defines the responses classes of trains according to the schema definition

@author Lukas Zimmermann
"""
from abc import ABC, abstractmethod
import json


class Response(ABC):

    @abstractmethod
    def to_dict(self):
        pass

    def to_json_string(self):
        return json.dumps(self.to_dict())


    # def as_json(self) -> str:
    #
    #     # Remove all the None values from the response dict
    #     d = without_none_values(self.as_response_dict())
    #
    #     # Replace the ResponseKeys by their String representation
    #     d = {key.value: value for key, value in d.items()}
    #
    #     # Return as a proper JSON string
    #     return json.dumps(d)
    #
    # @abc.abstractmethod
    # def as_response_dict(self) -> ResponseDict:
    #     pass


# class RunAlgorithmResponse(Response):
#
#     def __init__(self,
#                  success: bool,
#                  message: str,
#                  next_train_tag: str,
#                  docker_base_image: str,
#                  export_files: List[str]):
#         self.success = success
#         self.message = message
#         self.next_train_tag = next_train_tag
#         self.docker_base_image = docker_base_image
#         self.export_files = export_files
#
#     def as_response_dict(self) -> ResponseDict:
#         return {
#             ResponseKey.SUCCESS: self.success,
#             ResponseKey.MESSAGE: self.message,
#             ResponseKey.NEXT_TRAIN_TAG: self.next_train_tag,
#             ResponseKey.DOCKER_BASE_IMAGE: self.docker_base_image,
#             ResponseKey.EXPORT_FILES: self.export_files
#         }
#
#
#
# class CheckRequirementsResponse(Response):
#     def __init__(self, unmet: List[str]):
#         self.unmet = unmet
#
#     def as_response_dict(self) -> ResponseDict:
#         return {
#             ResponseKey.UNMET: self.unmet,
#         }
#
#
# class PrintSummaryResponse(Response):
#     def __init__(self, content: str):
#         self.content = content
#
#     def as_response_dict(self) -> ResponseDict:
#         return {
#             ResponseKey.CONTENT: self.content
#         }
