#!/usr/bin/env python3

# Notify LINE of temperature

import time
import redis
import requests
from setenv import RedisKeyValue,LINEtoken

RedisKey = "RPIvalue"
RedisHost = "redis-16303.c100.us-east-1-4.ec2.cloud.redislabs.com"
RedisPort = "16303"
RedisPwd = RedisKeyValue

def main():
    while True:
        r = redis.Redis(host=RedisHost, port=RedisPort, password=RedisPwd, db=0)
        ret = r.get(RedisKey)
        ondo = str(ret).split("'")
        ResultTemp = int(ondo[1][11:13])
        if ResultTemp >= 35:
            send_line_notify(ResultTemp)
            time.sleep(600)
        elif ResultTemp >= 30:
            send_line_notify(ResultTemp)
            time.sleep(1200)
        elif ResultTemp >= 27:
            send_line_notify(ResultTemp)
            time.sleep(1800)
        elif ResultTemp >= 24:
            send_line_notify(ResultTemp)
            time.sleep(3600)
        else :
            time.sleep(10)

def send_line_notify(NotifTemp):
        line_notify_token = LINEtoken
        line_notify_api = 'https://notify-api.line.me/api/notify'
        notification_message = '部屋の温度が' + str(NotifTemp) + '度を超えました。'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'message: {notification_message}'}
        requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()
