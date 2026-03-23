from rich import print as rprint
from rich.pretty import Pretty
from datetime import datetime

def format_output(name, value, location):
    value_type = type(value).__name__

    try:
        length = len(value)
        length_info = f", len={length}"
    except Exception:
        length_info = ""

    timestamp = datetime.now().strftime("%H:%M:%S")

    rprint(f"[dim]{timestamp}[/] [yellow]{location}[/]")
    rprint(f"[bold cyan]{name}[/] ([green]{value_type}{length_info}[/]):")
    rprint(Pretty(value, expand_all=True))
    rprint("-" * 50)