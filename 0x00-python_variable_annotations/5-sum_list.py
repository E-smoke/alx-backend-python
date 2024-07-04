#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
        Returns sum of the floats in the list.
    '''
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
