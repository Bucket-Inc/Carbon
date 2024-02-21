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


print("hello")
