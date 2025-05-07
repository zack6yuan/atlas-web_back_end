#!/usr/bin/env python3
# Method: Handle complex types
from typing import Union


def to_kv(k: str, v: [Union[int, float]]) -> tuple:
    value2 = v * v
    return (k, value2)