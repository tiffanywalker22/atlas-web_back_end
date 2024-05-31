#!/usr/bin/env python3
""" caching module that uses redis to store and retrieve data """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts number of times a method is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """logs the input and output of a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increments call count and logs method i/o history in"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable):
    """function to replay histotry of i/o for method"""
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_args.decode
              ('utf-8')}) -> {output.decode('utf-8')}")


class Cache:
    """ class representing cache with redis """
    def __init__(self):
        """ initalizes cache and makes connection to redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data in cache and returns key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """retrieves data from cache based on key"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """retrieves string value from cache"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: bytes) -> int:
        """retrieves integer value from cache"""
        return self.get(key, lambda d: int(d.decode("utf-8")))
