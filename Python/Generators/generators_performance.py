# generators are much more performant than lists. (i.e range > list in performance)
# So generators are really, really useful when calculating large sets of data

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000000): #it finishes after.
        i*5

long_time()


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)): #it took longer.
        i*5

long_time2()

'''
1
took 1.6450591087341309 s
2
took 2.45094895362854 s
'''

# generators are very efficient when we are looping through large sets of data