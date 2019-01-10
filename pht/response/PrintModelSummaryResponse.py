"""
Contains the PrintModelSummaryResponse class, which belongs to the print_model_summary class.

@author Lukas Zimmermann
"""
from .Response import Response


class PrintModelSummaryResponse(Response):
    """
    Response for the print_model_summary command
    """
    def __init__(self, content):
        self.content = content

    @property
    def type(self):
        return 'PrintModelSummaryResponse'

    def to_dict(self):
        return {
            'type': self.type,
            'content': self.content
        }
