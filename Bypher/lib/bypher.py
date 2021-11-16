#!/usr/bin/env python3

from os import path
from sys import stderr as STDERR
from itertools import chain
from random import choice as rndCh
from string import ascii_letters as letters

from lib import ask

# Binary representation of each character
BIN_REP = "0:0{}b"


def _print_result(text: str, out_method: int) -> None:
    """Print the text after applying the operation specified by the user.

    Parameters
    ----------
    text: str - Text to print
    out_method: int - Flag for the output method (0 - File | 1 - Console)

    """
    if (out_method == 0):
        # File
        while True:
            file_path = _read_path(input("-- Path to file: "))
            try:
                open(file_path, "wa").write(text)
                break
            except PermissionError:
                print("*** Permission dennied: '{}' ***".format(file_path),
                      file=STDERR)
    else:
        # Stdout
        print("\n-- Message --")
        print(text)


def _read_path(file_path: str) -> str:
    """Read the path to a file (absolute or relative).

    Parameters
    ----------
    file_path: str - Path to the file (absolute or relative)

    Returns
    -------
    str - Absolute path to the file

    """
    if file_path[0] == '~':
        return path.abspath(file_path[1:])
    return file_path


def _read_text(in_method: int, perm_len: int) -> str:
    """Read the text to cypher/decypher (from file or console).

    Parameters
    ----------
    in_method: int - Flag for the input method (0 - File | 1 - Console)

    Returns
    -------
    str - Users' text (either from a file or console)

    """
    res = ""
    if (in_method == 0):  # File
        while True:
            f_path = _read_path(input("-- Path to file: "))
            try:
                res = open(f_path, "r").read()
                break  # If no exception, exit loop
            except FileNotFoundError:
                print("*** No such file or directory: '{}' ***".format(f_path),
                      file=STDERR)
            except PermissionError:
                print("*** Permission dennied: '{}' ***".format(f_path),
                      file=STDERR)
    else:  # Stdin
        print("\n-- Type the message --\n\n")
        while True:
            txt = input()+'\n'
            if txt == '\n':
                break
            res += txt
    # Add random chars if text length is not multiple of permitations
    return res if len(res) % perm_len == 0 else res+perm_len*rndCh(letters)


def _sliding_window(raw_text: str, perm_len: int) -> [[int]]:
    """Create a list of lists of each permutation group.

    Parameters
    ----------
    raw_text: str - Text to cypher/decypher
    perm_len:int - Length of permutations group (1st key)

    Returns
    -------
    [[str]] - List of permutations groups (lists)

    """
    return [raw_text[i:i+perm_len]
            for i in range(0, len(raw_text), perm_len)]


def _turn_to_binary(text_groups: [[str]], bin_format: str) -> [[str]]:
    """Create a list of lists with eahc permutation group on binary format.

    Parameters
    ----------
    text_groups: list(list(str)) - Permutations groups on 2D lists
    bin_format: str - Binary format to use for each character

    Returns
    -------
    [[str]] . List of permutations groups (list) on binary format each char

    """
    return [[bin_format.format(ord(a)) for a in b] for b in text_groups]


def _cypher(in_method: int, perm_len: int, bin_format: str) -> str:
    """Cypher users' text.

    Parameters
    ----------
    in_method: int - Flag for the input method (0 - File | 1 - Console)
    perm_len: int - Length of permutations group (1st key)
    bin_format: str - Binary format to use for each character

    Returns
    -------
    str - Cyphered text

    """
    coded_text = ""
    raw_text = _read_text(in_method, perm_len)
    for block in _turn_to_binary(
            _sliding_window(raw_text, perm_len),
            bin_format):
        coded_text += ''.join(list(chain.from_iterable(zip(*block))))
    return coded_text


def _decypher(in_method: int, perm_len: int, letter_len: int) -> str:
    """Decypher users' text.

    Parameters
    ----------
    in_method: int - Flag for the input method (0 - File | 1 - Console)
    perm_len: int - Length of permutations group (1st key)
    letter_len: int - Length of each character binary representation (2nd key)

    Returns
    -------
    str - Decyphered text

    """
    clear_txt = ""
    raw_text = _read_text(in_method, perm_len)
    ptr_1 = 0
    for ptr_2 in range(perm_len*letter_len, len(raw_text)+1,
                       perm_len*letter_len):
        line = raw_text[ptr_1:ptr_2]
        for i in range(perm_len):
            clear_txt += chr(int(line[i::perm_len], 2))
            ptr_1 = ptr_2
    return clear_txt


def main():
    """Byphers' main function."""
    try:
        op = ask._operation()
        # key[0] = len of permutation groups
        # key[1] = len of representation
        key = ask._key()
        in_method = ask._input_method()
        out_method = ask._output_method()
        if op == 0:
            new_txt = _cypher(
                in_method, key[0], "{"+"0:0{}b".format(key[1])+"}")
        elif op == 1:
            new_txt = _decypher(
                in_method, key[0], key[1])
        else:
            print("*** Operation not supported ***", file=STDERR)
            exit(1)
        _print_result(new_txt, out_method)
    except (TypeError, ValueError, KeyboardInterrupt):
        print("*** You can't do that :P **", file=STDERR)
        exit(-1)
    exit(0)


if __name__ == "__main__":
    main()
