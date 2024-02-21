import json
import rich
import shlex
from rich.console import Console

console = Console()

class version:
    version = "0.0.1"
    branch = "dev"

def print(string, color=None):
    console.print(string, style=color)


def parse_arguments():
    input_str = input("> ")

    # Split input string into arguments using shlex
    args = shlex.split(input_str)

    # Quote each argument using shlex.quote()
    quoted_args = [shlex.quote(arg) for arg in args]

    return quoted_args

