#!/usr/bin/env python3
'''
A type-annotated function
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Function that uses union &accept str,int por float to return tuple
    '''
    return (k, float(v**2))
