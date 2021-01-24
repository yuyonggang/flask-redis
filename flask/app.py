from flask import Flask, render_template
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', '192.168.100.236'), port=6379)

@app.route('/')

def hello():
    redis.incr('hits')
#    return 'Hello app.py Container World! I have been seen %s times and my hostname is %s.\n' % (redis.get('hits'),socket.gethostname())
    url = 'Hello index Container World! I have been seen %s times and my hostname is %s.\n' % (redis.get('hits'),socket.gethostname())
    return render_template('index.html', url=url)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
