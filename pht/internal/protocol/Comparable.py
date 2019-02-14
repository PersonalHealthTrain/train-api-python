import abc


class Comparable(abc.ABC):
    """
    Class implementing this interface are meant to be safe to be compared via the '==' operator
    """
    @abc.abstractmethod
    def __eq__(self, other):
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass
