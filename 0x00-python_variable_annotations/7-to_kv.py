#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
        Returns a tuple.
    '''
    tup = (k, float(v**2))
    return tup
