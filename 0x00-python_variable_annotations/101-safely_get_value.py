#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import Union, Tuple, Iterable, Sequence, List, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default = Union[T, None]) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
