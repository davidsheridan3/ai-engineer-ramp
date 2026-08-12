# Decorator
from time import time
def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Took {t2-t1} ms')
        return result
    return wrap_func




@performance
def long_time():
    for i in range(1000000000):
        i*5

long_time()

# very useful to test performance of functions before deployment