import abc


class Formula:

    @property
    @abc.abstractmethod
    def type(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def display(self) -> str:
        pass

    @abc.abstractmethod
    def to_dict(self):
        pass
