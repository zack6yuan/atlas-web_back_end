#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        pass
    return wrapper

def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(str(args))
    return wrapper

def replay():
    pass


class Cache:
    """ Cache Class """
    def __init__(self):
        """ init method """
        self._redis = redis.Redis() # Store an instance of redis
        self._redis.flushdb()

    @count_calls
    @call_history
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
        new_key = str(uuid.uuid4())
        self._redis.set(new_key, data)
        
        return new_key
    
    def get(key, fn: Optional[Callable]):
        if key is None:
            return None
        
            
    def get_str(self):
        """ Get Self Function """
        pass
    
    def get_int(self):
        """ Get Int Function """
        