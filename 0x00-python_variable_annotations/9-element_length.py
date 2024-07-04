#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import Union, Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''function'''

    return [(i, len(i)) for i in lst]
