import abc


class DictRepresentable(abc.ABC):

    @abc.abstractmethod
    def as_dict(self):
        pass
