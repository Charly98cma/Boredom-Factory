from sys import stderr as STDERR
from random import choice as rndCh
from string import ascii_letters as letters
from os import path

from lib import err_msgs as err


def __print_file(text: str):
    file_path = read_path(input("-- Path to file: "))
    try:
        with open(file_path, mode='a', encoding='UTF-8') as f:
            f.write(text)
    except PermissionError:
        print(err.permission_error(file_path), file=STDERR)


def __print_console(text: str):
    print("\n-- Message --")
    print(text)


PRINT_METHODS = {
    0: __print_file,
    1: __print_console
}


def print_result(text: str, out_method: int) -> None:
    """Print the text after applying the operation specified by the user.


    Parameters
    ----------
    text: str - Text to print
    out_method: int - Flag for the output method (0 - File | 1 - Console)

    """
    PRINT_METHODS[out_method](text)


def read_path(file_path: str) -> str:
    """Read the path to a file (absolute or relative).


    Parameters
    ----------
    file_path: str - Path to the file (absolute or relative)


    Returns
    -------
    str - Absolute path to the file

    """
    return path.abspath(file_path[1:]) if file_path[0] == '~' else file_path


def read_text_file():
    """
    Reads user input from a file
    """
    while True:
        file_path = read_path(input("-- Path to file: "))
        try:
            return open(file_path, 'r', encoding='UTF-8').read()
        except FileNotFoundError:
            print(err.file_error(file_path), file=STDERR)
        except PermissionError:
            print(err.permission_error, file=STDERR)


def read_text_stdin():
    """
    Reads user input from standard input.
    """
    print("\n-- Type the message --\n\n")
    res = ""
    while True:
        if (txt := input()+'\n') == '\n':
            break
        res += txt
    return res


def read_text(in_method: int, perm_len: int) -> str:
    """Read the text to cypher/decypher (from file or console).


    Parameters
    ----------
    in_method: int - Flag for the input method (0 - File | 1 - Console)


    Returns
    -------
    str - Users' text (either from a file or console)

    """
    res = read_text_file() if in_method == 0 else read_text_stdin()
    # Add random chars if text length is not multiple of permitations
    return res if len(res) % perm_len == 0 else res+perm_len*rndCh(letters)
