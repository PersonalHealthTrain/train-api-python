def type_is_int(obj):
    if not isinstance(obj, int) or isinstance(obj, bool):
        raise TypeError("Object '{}' is required to be of type int".format(str(obj)))


def for_value(val, func, msg):
    if not func(val):
        raise ValueError(msg)


def is_not_none(val):
    return val is not None
