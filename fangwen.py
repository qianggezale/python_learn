# utf-8


def _add(*arg):
    sum = 0
    for n in arg:
        sum = sum + n
    return sum


def add(*arg):
    return _add(*arg)
