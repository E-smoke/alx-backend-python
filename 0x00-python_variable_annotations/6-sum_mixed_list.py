#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
        Returns sum of the floats in the list.
    '''
    sum: float = 0
    for i in mxd_lst:
        sum += i
    return sum
