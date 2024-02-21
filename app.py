import json
import rich
import shlex
from rich.console import Console

console = Console()

class version:
    version = "0.0.1"
    branch = "dev"

def print(string, color=None):
    """
    Print a string with optional color.

    Args:
        string (str): The string you want to print.
        color (str, optional): The color you want the string to be.
    """
    console.print(string, style=color)


def parse_arguments():
    """
    Parse arguments from the included input.

    Returns:
        list: The command (index: 0) and the arguments.
    """
    input_str = input("> ")

    # Split input string into arguments using shlex
    args = shlex.split(input_str)

    # Quote each argument using shlex.quote()
    quoted_args = [shlex.quote(arg) for arg in args]

    return quoted_args


def read_json(filename):
    """
    Read data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The data read from the JSON file.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{filename}': {e}")
        return None

def write_json(filename, data):
    """
    Write data to a JSON file.

    Args:
        filename (str): The path to the JSON file.
        data (dict): The data to be written to the JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to '{filename}'.")
    except TypeError as e:
        print(f"Error writing JSON to '{filename}': {e}")

