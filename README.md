# redis-ratelimit

![Travis](https://img.shields.io/travis/romantomjak/redis-ratelimit.svg)
![Coveralls](https://img.shields.io/coveralls/github/romantomjak/redis-ratelimit.svg)
![PyPI](https://img.shields.io/pypi/v/redis-ratelimit.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/redis-ratelimit.svg)

A fixed window rate limiter based on Redis

---

## Installation

```shell
$ pip install redis-ratelimit
```

## Example Usage

The library itself is framework agnostic, but let's assume you want to use it with [Flask](http://flask.pocoo.org/docs/0.12/):

```python
from http import HTTPStatus # python 3.4 +
from flask import Flask, jsonify
from flask import make_response
from redis_ratelimit import ratelimit
from redis_ratelimit.exceptions import RateLimited

app = Flask(__name__)

@app.route('/')
@ratelimit(rate='2/s', key='ccc')
def index():
    return jsonify({'status': 'OK'})

def over_limit(e):
    code = HTTPStatus.TOO_MANY_REQUESTS # 429
    body = jsonify({"message":str(e)})
    return make_response(body, code.value)

app.register_error_handler(RateLimited, over) # flask error handler

if __name__ == '__main__':
    app.run()
```

This will allow a total of 10 requests in any given minute, but no faster than 2 requests a second.

## Notes

- [Redis Rate Limiting Pattern #2](https://redis.io/commands/INCR#pattern-rate-limiter-2)

## License

MIT