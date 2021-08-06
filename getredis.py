#!/usr/bin/env python3

import time
import redis

RedisKey = "RPIvalue"

RedisHost = "redis-16303.c100.us-east-1-4.ec2.cloud.redislabs.com"  
RedisPort = "16303"
RedisPwd = "CTFaaddfoG014Km6QC6QQ1ueaKh9hIE3"

r = redis.Redis(host=RedisHost, port=RedisPort, password=RedisPwd, db=0)
ret = r.get(RedisKey)
print(ret)
