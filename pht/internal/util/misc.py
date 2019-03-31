from typing import Any, Iterable, Optional
from pht.internal.protocol.SimpleMappingRepresentable import SimpleMappingRepresentable
from pht.internal.protocol.DeepCopyable import DeepCopyable


def frozen_set_of(typ, item, more_items: Iterable[Any]):
    if not isinstance(item, typ):
        raise TypeError('Item \'{}\' is not of type: \'{}\''.format(str(item), str(typ)))
    tmp = set(more_items)
    tmp.add(item)
    for i in tmp:
        if not isinstance(i, typ):
            raise TypeError('Item \'{}\' is not of type: \'{}\''.format(str(i), str(typ)))
    return frozenset(tmp)


def _do_or_none(x, f):
    return f(x) if x is not None else None


def as_simple_mapping_or_none(item: Optional[SimpleMappingRepresentable]):
    """
    Returns the SimpleMap Representation of item if present, None otherwise
    """
    return _do_or_none(item, lambda x: x.as_simple_mapping())


def deepcopy_or_none(item: Optional[DeepCopyable]):
    """
    Returns Deepcopy of item if present, else None
    """
    return _do_or_none(item, lambda x: x.deepcopy())
