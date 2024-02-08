import time
import logging
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
        start_time = time.perf_counter()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.perf_counter()  # Record end time
        runtime = end_time - start_time  # Calculate runtime
        print(f"Runtime: {runtime:.6f} seconds")  # Print runtime
        return result
    return wrapper
