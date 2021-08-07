#!/usr/bin/env python3

import time
import redis
from setenv import RedisKeyValue

RedisKey = "RPIvalue"

RedisHost = "redis-16303.c100.us-east-1-4.ec2.cloud.redislabs.com"  
RedisPort = "16303"
RedisPwd = RedisKeyValue

r = redis.Redis(host=RedisHost, port=RedisPort, password=RedisPwd, db=0)
ret = r.get(RedisKey)
print(ret)

print(ret[11:15])
print(ret[26:30])

