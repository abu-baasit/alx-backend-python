#!/usr/bin/env python3
'''
A type-annotated function
'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''function that takes mixed list and return float
    '''
    return (sum(mxd_lst))
