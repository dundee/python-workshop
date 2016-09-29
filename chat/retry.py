from functools import wraps
import time


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwds):
            last_exc = None
            for _ in range(count):
                try:
                    return func(*args, **kwds)
                except Exception as exc:
                    last_exc = exc
                    time.sleep(0.5)
                    continue
            raise last_exc
        return wrapper
    return decorator
