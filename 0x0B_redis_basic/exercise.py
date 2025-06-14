#!/usr/bin/env python3
from typing import String, Union
import uuid


class Cache:
    """ Cache Class """
    def __init__(self):
        """ init method """
        pass

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Params:
            self --> instance of the class
            data --> data argument
        Methods:
            generates a random key --> uuid
            stores input data in Redis with random key
        Returns:
            the key
        """
        new_key = uuid.uuid4()
        input_data = redis.Redis()
        
