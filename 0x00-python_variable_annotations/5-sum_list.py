#!/usr/bin/env python3
'''
A type-annotated function
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''take a list of float and return summation value 
    '''
    return float(sum(input_list))
