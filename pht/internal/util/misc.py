from typing import Any, Iterable, Optional
from pht.internal.protocol.DictRepresentable import DictRepresentable
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


def as_dict_or_none(item: Optional[DictRepresentable]):
    return item.as_dict() if item is not None else None


def copy_or_none(item: Optional[Copyable]):
    return item.copy() if item is not None else None
