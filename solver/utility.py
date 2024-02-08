import time
from functools import wraps


def record_runtime(func):
    """Decorator to record run-time of functions

    Args:
        func (func): function to be timed

    Returns:
        functools.wraps: wrapper
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time

        print(f"Runtime: {runtime:.6f} seconds")

        return result

    return wrapper
