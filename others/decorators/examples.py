# timing a function

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def add(a, b):
    return a + b

add(3, 5)