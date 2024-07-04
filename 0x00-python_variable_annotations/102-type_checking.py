#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import Union, Tuple, Iterable, Sequence, List, Any, Mapping


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''function'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
