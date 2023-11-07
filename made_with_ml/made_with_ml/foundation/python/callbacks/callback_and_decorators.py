"""
Putting it all together, decorators and callbacks
"""

from functools import wraps

# Decorator
def add(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        """Wrapper function for add"""
        x = kwargs.pop("x")
        x += 1
        x = f(*args, **kwargs, x=x)
        x += 1
        return x
    return wrap

# Callback
class x_tracker(object):
    def __init__(self, x):
        self.history = []
    def at_start(self, x):
        self.history.append(x)
    def at_end(self, x):
        self.history.append(x)

# Main function
def operations(x, callbacks=[]):
    """Basic operations."""
    for callback in callbacks:
        callback.at_start(x)
    x += 1
    for callback in callbacks:
        callback.at_end(x)
    return x

x = 1
tracker = x_tracker(x=x)
print(operations(x=x, callbacks=[tracker]))

print(tracker.history)

print(operations.__doc__)