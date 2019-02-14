import abc


class Copyable(abc.ABC):
    """
    Marks a class to be copyable and requires implementation of Copy.
    Generally, implementors should not distinguish between flat copy and
    deep copy.
    """
    @abc.abstractmethod
    def copy(self):
        pass

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()
