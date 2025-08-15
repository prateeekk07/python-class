# Control Flow->

# conditional statement -- if, elif, else
# iterative statement -- for, while loop
# transfer statement  -- break, continue, pass

from flask import Flask, request
from flask_caching import Cache
import time

app = Flask(__name__)

# Configure Flask-Caching with Redis
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
app.config['CACHE_DEFAULT_TIMEOUT'] = 30  # 30 seconds

cache = Cache(app)

# Example route with caching
@app.route('/data')
@cache.cached(timeout=60)  # Cache this endpoint for 10 seconds
def get_data():
    time.sleep(3)  # Simulating a slow function
    return {"message": "Here is your data!"}

if __name__ == "__main__":
    app.run(debug=True)
