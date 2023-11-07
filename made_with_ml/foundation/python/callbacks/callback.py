"""
Demonstrates callbacks: conditional/situational processing withing the function
"""
# Callbacks
class x_tracker(object):
    def __init__(self, x):
        self.history = []
    def at_start(self, x):
        self.history.append(x)
    def at_end(self, x):
        self.history.append(x)

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