#!/usr/bin/env python3

import redis
redis = redis.Redis()
print(redis.set('test1', 1))
print(redis.get('test1'))

