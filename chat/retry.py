from functools import wraps
import logging
import time


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwds):
            last_exc = None
            for attempt in range(count):
                try:
                    return func(*args, **kwds)
                except Exception as exc:
                    logging.debug('%s failed, retry %d / %d', func.__name__, attempt, count)
                    last_exc = exc
                    time.sleep(0.5)
                    continue
            raise last_exc
        return wrapper
    return decorator
