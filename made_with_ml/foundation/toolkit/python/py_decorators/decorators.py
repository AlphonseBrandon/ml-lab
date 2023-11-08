"""
Aumenting a function with pre/post processing with decorators
"""
from functools import wraps
# Creating a decorator
def add(f):
    """Basic operations function decorator"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        """Wrapper function for add."""
        x = kwargs.pop("x") # get x
        x += 1 # execute before function f
        x = f(*args, **kwargs, x=x)
        x += 1 # execute after the function f
        return x
    return wrapper

@add
def operations(x):
    "Basic operations."
    x += 2
    return x

print(operations(x=1))

print(operations.__name__, operations.__doc__)
