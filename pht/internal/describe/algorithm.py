import abc


class AlgorithmRequirement(abc.ABC):

    @abc.abstractmethod
    def to_dict(self):
        pass
