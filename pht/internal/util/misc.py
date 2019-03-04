from typing import Any, Iterable, Optional
from pht.internal.protocol.SimpleDictRepresentable import SimpleDictRepresentable
from pht.internal.protocol.Copyable import Copyable


def frozen_set_of(typ, item, items: Iterable[Any]):
    if not isinstance(item, typ):
        raise TypeError('Item \'{}\' is not of type: \'{}\''.format(str(item), str(typ)))
    tmp = {i for i in items}
    tmp.add(item)
    for i in tmp:
        if not isinstance(i, typ):
            raise TypeError('Item \'{}\' is not of type: \'{}\''.format(str(i), str(typ)))
    return frozenset(tmp)


def _do_or_none(x, f):
    return f(x) if x is not None else None


def as_dict_or_none(item: Optional[SimpleDictRepresentable]):
    return _do_or_none(item, lambda x: x.as_simple_dict())


def copy_or_none(item: Optional[Copyable]):
    return _do_or_none(item, lambda x: x.copy())
