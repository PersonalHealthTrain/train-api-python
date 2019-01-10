class IllegalResponse(Exception):
    """
    Error that should be thrown if an illegal response is tried to be created.
    """
    def __init__(self, message):
        super().__init__(message)
