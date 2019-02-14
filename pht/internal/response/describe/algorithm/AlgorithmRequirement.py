import abc
from pht.internal.protocol.Comparable import Comparable
from pht.internal.protocol.Copyable import Copyable
from pht.internal.protocol.Typed import Typed


class AlgorithmRequirement(Comparable, Copyable, Typed, abc.ABC):
    pass
