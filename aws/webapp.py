#!/usr/bin/env python3

# Import modules required for app

import time
import redis
import os
from flask import Flask, render_template, request
from setenv import RedisKeyValue

# Create a Flask instance
app = Flask(__name__)

##### Define routes #####
@app.route('/')
def home():
    RedisKey = "RPIvalue"

    RedisHost = "redis-16303.c100.us-east-1-4.ec2.cloud.redislabs.com"
    RedisPort = "16303"
    RedisPwd = RedisKeyValue

    while True:
        r = redis.Redis(host=RedisHost, port=RedisPort, password=RedisPwd, db=0)
        ret = r.get(RedisKey)
        # print(str(ret))    # for debug
        ondo = str(ret).split("'")
        # print(ondo[1])     # for debug
        values = {"val1":ondo[1][11:15], "val2":ondo[1][26:30]}
        return render_template('index.html', values=values)

##### Run the Flask instance, browse to http://<< Host IP or URL >>:5000 #####
if __name__ == "__main__":
        app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
