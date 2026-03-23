import inspect
from typing import Any

def get_var_names():
    frame = inspect.currentframe().f_back.f_back
    code = inspect.getframeinfo(frame).code_context

    if not code:
        return ["value"]

    line = code[0]
    if "log(" not in line:
        return ["value"]

    inside = line.split("log(")[1].split(")")[0]
    return [x.strip() for x in inside.split(",")]


def get_location():
    frame = inspect.currentframe().f_back.f_back
    info = inspect.getframeinfo(frame)
    return f"{info.filename}:{info.lineno}"


def truncate(value: Any, max_items: int):
    if isinstance(value, (list, tuple, set)) and len(value) > max_items:
        return list(value)[:max_items] + ["..."]
    if isinstance(value, dict) and len(value) > max_items:
        return dict(list(value.items())[:max_items])
    return value