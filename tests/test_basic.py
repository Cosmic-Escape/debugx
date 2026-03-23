from debugx import log, diff

def test_log_runs():
    log(123)

def test_diff_runs():
    diff("x", 1)
    diff("x", 2)