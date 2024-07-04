#!/usr/bin/env python3

'''
    Basic annotations for variables.
'''

from typing import Union, Tuple, Iterable, Sequence, List, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''function'''

    if lst:
        return lst[0]
    else:
        return None
