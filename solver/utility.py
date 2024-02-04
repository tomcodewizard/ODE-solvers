import time
import logging



def record_run_time(func):

    level = logging.INFO
    fmt = '[%(levelname)s] - %(message)s'    
    logging.basicConfig(level=level, format=fmt)

    def wrapper(*args, **kwargs):

        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter() - t1
        logging.info(f'{func.__name__}() took {t2} seconds')

    return wrapper()
