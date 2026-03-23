from debugx import log, timeit, diff

# Basic logging
x = [1, 2, 3, 4, 5, 6, 7, 8]
name = "Debugx"

log(x, name, label="User Data")

# Diff tracking
diff("counter", 1)
diff("counter", 5)

# Timing example
@timeit
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

slow_function()