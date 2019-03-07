from abc import ABC, abstractmethod


class Copyable(ABC):
    """
    Marks a class to be copyable and requires implementation of copy(). The idea is that copying becomes
    an explicit operation on the objects and that there is no distinction between __copy__ and __deepcopy__.
    The copy() method should implement copy() with the semantics of __deepcopy__.
    """
    @abstractmethod
    def copy(self):
        """
        Copies the object. Implementation should perform a deepcopy, i.e. each modification at the copied value
        does not reflect in the original one.
        """
        pass

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()
