import abc


class DictRepresentable(abc.ABC):
    """
    Classes implementing this protocol have a canonical represenation as a dictionary
    """
    @abc.abstractmethod
    def as_dict(self) -> dict:
        pass

