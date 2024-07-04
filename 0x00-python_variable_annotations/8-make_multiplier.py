#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import Callable, Union, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        Returns a function.
    '''
    def f(n: float) -> float:
        '''returns a float'''
        return float(n * multiplier)
    return f
