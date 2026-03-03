from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    count = r.incr('hits')
    return f'''
    <html>
    <head><title>Redis Hit Counter</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Docker + Redis App</h1>
        <p>This page has been visited <strong>{count}</strong> time(s).</p>
        <p><em>Powered by Flask and Redis</em></p>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    try:
        r.ping()
        return {'status': 'ok', 'redis': 'connected'}, 200
    except Exception as e:
        return {'status': 'error', 'redis': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
