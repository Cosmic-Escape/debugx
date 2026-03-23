# Debugx

**Smart debugging for Python developers.**  
Stop using `print()`. Start debugging smarter.

---

## Features

Debugx is designed to make debugging **fast, intuitive, and visually clear**. Key features include:

| Feature | Function / Method | Description |
|---------|-----------------|-------------|
| **Automatic variable detection** | `log(var)` | Logs variable name, type, and value without manually typing names. |
| **Pretty output** | `log(var)` | Uses `rich` for colorful, structured formatting. |
| **Large data truncation** | `log(var)` | Automatically truncates large lists, dicts, and strings for readability. |
| **File & line tracking** | `log(var)` | Shows where the log was called in your code. |
| **Timestamped logs** | `log(var)` | Includes timestamp for each log entry. |
| **Multi-variable logging** | `log(var1, var2, ...)` | Logs multiple variables in one call. |
| **Execution time measurement** | `timeit(func)` | Measures and prints function execution time. |
| **Value diff tracking** | `diff(name, old_value, new_value)` | Tracks changes in a variable over time. |
| **Exception handling** | `catch(func)` | Logs exceptions neatly without stopping your program. |
| **Nested structure logging** | `log(obj)` | Supports nested dicts, lists, tuples, etc. |
| **Loop debugging** | `log_loop(var)` | Logs each iteration of a loop. |
| **Flexible configuration** | `config.py` | Customize colors, truncation, and timestamp formats. |
| **Easy integration** | Works with any Python project | Just `pip install -e .` or import directly. |
| **Extensible** | Add your own formatters | Fully modular for custom debugging needs. |
| **Example scripts** | `examples/` | Ready-to-run demos to learn every feature quickly. |

---

## Installation

Install directly from the source for editable development:

```bash
pip install -e .

```
or clone and install:
git clone https://github.com/Cosmic-Escape/dubugx.git
cd debugx
pip install -e .

## Quickstart Example
```python
from debugx import log, diff, timeit, catch

# === BASIC LOGGING ===
x = [1, 2, 3, 4]
log(x)

name = "Debugx"
log(x, name)

# === DIFF TRACKING ===
counter = 1
diff("counter", counter, 5)

# === TIMING ===
@timeit
def slow_function():
    sum(range(100000))
slow_function()

# === EXCEPTION HANDLING ===
def risky():
    return 1 / 0

catch(risky)

# === NESTED STRUCTURES ===
data = {
    "user": "verma",
    "scores": [10, 20, 30],
    "meta": {"active": True, "level": 3}
}
log(data)

# === LOOP DEBUGGING ===
for i in range(3):
    log(i)

```

## Contributing
Debugx is open source and welcomes contributions!

Steps to contribute:

Fork the repository on GitHub.

Create a new branch:

git checkout -b feature/my-feature
Make your changes or add new features.

Run tests in tests/ to ensure everything works:

python -m unittest discover tests

Commit your changes:

git commit -am "Add my new feature"

Push to your fork:

git push origin feature/my-feature
Open a Pull Request on GitHub.

Guidelines:

Follow PEP8 for Python code.
Add docstrings for all new functions.
Include tests for any new functionality.