import sys
import os
import string
from random import shuffle, sample

def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def read_table_from_file(file_name, separator=';'):
    """Read CSV file into a data table.

    Args:
        file_name: The name of the CSV data file.
        separator: The CSV separator character

    Returns:
        The data parsed into a list of lists.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []


def write_table_to_file(file_name, table, separator=';'):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.
        table: list of lists containing tabular data.
        separator: The CSV separator character
    """
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")


def make_dict(data, headers):
    return [{headers[i]: stat for i, stat in enumerate(line)} for line in data]


def generate_id():
    small_letters = [chr(x) for x in range(97, 123)]
    capital_letters = [chr(x) for x in range(65, 91)]
    numbers = [chr(x) for x in range(48, 58)]
    spec_chars = ['_', '-', '+', '!']
    while True:
        new_id = sum([sample(small_letters, 4), sample(capital_letters, 2), sample(numbers, 2), sample(spec_chars, 2)],
                     [])
        shuffle(new_id)
        return ''.join(new_id)
