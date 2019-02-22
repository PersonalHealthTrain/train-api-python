from typing import Any, Iterable
from pht.internal.protocol.DictRepresentable import DictRepresentable


def frozen_set_of(typ, item, items: Iterable[Any]):
    if not isinstance(item, typ):
        raise TypeError('Item \'{}\' is not of type: \'{}\''.format(str(item), str(typ)))
    tmp = {i for i in items}
    tmp.add(item)
    for i in tmp:
        if not isinstance(i, typ):
            raise TypeError('Item \'{}\' is not of type: \'{}\''.format(str(i), str(typ)))
    return frozenset(tmp)


def as_dict_or_none(item: DictRepresentable):
    return item.as_dict() if item is not None else None
