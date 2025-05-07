#!/usr/bin/env python3
# Method: Handle complex types
from typing import Union, Tuple

# Give a type hint to the tuple that will be returned
def to_kv(k: str, v: [Union[int, float]]) -> Tuple[str, Union[int, float]]:
    value2 = v * v
    return (k, value2)