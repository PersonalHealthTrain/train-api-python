import abc
from pht.internal.protocol import Comparable, Copyable, Typed


class AlgorithmRequirement(Comparable, Copyable, Typed, abc.ABC):
    pass
