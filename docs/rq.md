RQ (_Redis Queue_) is a simple Python library for queueing jobs and processing
them in the background with workers.  It is backed by Redis.

RQ requires Redis >= 3.0.0.

## Getting started

First, run a Redis server, of course:

```console
$ redis-server
```

Then, create an RQ queue:

```python
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

def testing():
    print('Testing')
```

And enqueue the function call:

```python
import redis_queue
redis_queue.queue.enqueue(redis_queue.testing)
```

### The worker

To start executing enqueued function calls in the background, start a worker
from your project's directory:

```console
$ rq worker
*** Listening for work on default
Got count_words_at_url('http://nvie.com') from default
Job result = 818
*** Listening for work on default
```

That's about it.


## Installation

Simply use the following command to install the latest released version:

    pip install rq

## Project history

This project has been inspired by the good parts of [Celery][1], [Resque][2]
and [this snippet][3], and has been created as a lightweight alternative to the
heaviness of Celery or other AMQP-based queueing implementations.


[r]: http://python-requests.org
[d]: http://python-rq.org/
[m]: http://pypi.python.org/pypi/mailer
[p]: http://docs.python.org/library/pickle.html
[1]: http://www.celeryproject.org/
[2]: https://github.com/resque/resque
[3]: http://flask.pocoo.org/snippets/73/
