from functools import reduce, partial, wraps, lru_cache 

@lru_cache(maxsize=128)
def fibonacci(n):
    if n<2: 
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

print(reduce(lambda x, y: x + y, [1,2,3,4,5], 10))

def multiply(x, y):
    return x * y
double = partial(multiply, 2)
print(double(5))

def my_decorator(func):
    """A decorator that wraps a function and preserves its metadata."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function that adds additional behavior to the decorated function."""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    """Function that prints a greeting message."""
    print(f"Hello, {name}!")
    print(say_hello.__name__)  
    print(say_hello.__doc__)   

say_hello("Alice")