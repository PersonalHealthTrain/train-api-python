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

    def to_dict(self):
        return {
            'type': self.type,
            'display': self.display,
            'value': self.value()
        }

    @abc.abstractmethod
    def value(self) -> dict:
        """
        Dictionary representing the value of a formula. The concrete implementation of the formula
        decides how this dictionary looks like
        """
        pass
