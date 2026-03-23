from .utils import get_var_names, truncate, get_location
from .formatter import format_output
from .config import DEBUG, MAX_ITEMS
import time
from functools import wraps

# =========================
# MAIN LOG FUNCTION
# =========================
def log(*values, label=None):
    if not DEBUG:
        return

    names = get_var_names()
    location = get_location()

    if label:
        print(f"\n=== {label} ===")

    for name, value in zip(names, values):
        value = truncate(value, MAX_ITEMS)
        format_output(name, value, location)


# =========================
# TIME MEASURE DECORATOR
# =========================
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"\n⏱ {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


# =========================
# DIFF TRACKER
# =========================
_previous_values = {}

def diff(name, value):
    global _previous_values

    old = _previous_values.get(name)

    print(f"\n Diff for '{name}':")

    if old is None:
        print("First value:", value)
    else:
        print("Old:", old)
        print("New:", value)

    _previous_values[name] = value