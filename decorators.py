def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def my_function():
    print("This is my function.")


my_function() #-->

"""
Before the function is called.
This is my function.
After the function is called.
"""

#-------------------------------------------------------------------

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start} seconds to run.")
        return result
    return wrapper

@time_it
def my_function():
    time.sleep(1)

my_function() #-->

"""Function my_function took 1.0020818710327148 seconds to run."""
