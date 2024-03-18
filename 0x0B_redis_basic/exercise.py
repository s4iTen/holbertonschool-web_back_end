#!/usr/bin/env python3
'''this is the redis exercise'''
import redis
from uuid import uuid4
from typing import Union


class Cache():
    def __init__(self):
        """this is the cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ this method generate a uniq key value for the
        data that is comming to it and store it"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
