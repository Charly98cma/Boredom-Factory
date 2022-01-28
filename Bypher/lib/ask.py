from getpass import getpass
from sys import stderr as STDERR

OP_ERROR = "*** INVALID OPERATION ***"
KEY_ERROR = "*** INVALID KEY ***"
INPUT_ERROR = "*** INVALID INPUT ***"
OUTPUT_ERROR = "*** INVALID OUTPUT ***"


def operation() -> int:
    """Ask the user for the operation (Cypher or Decypher).


    Returns
    -------
    int - Operation chosen (0 - Cypher | 1 - Decypher)

    """
    while True:
        print("-- Select operation --\n0 - Cypher | 1 - Decypher")
        op = int(input())
        if op in {0, 1}:
            break
        print(OP_ERROR, file=STDERR)
    return op


def key() -> [int]:
    """Ask the user for the key (2 integers).


    Returns
    -------
    list() - Two integers (permutations length, and binary format length)

    """
    key_l = [0, 0]
    while True:
        key_l[0] = (int(getpass("\n-- Enter first key: ")))
        key_l[1] = (int(getpass("-- Enter second key: ")))
        if key_l[0] >= 2 and key_l[1] >= 8:
            break
        print(KEY_ERROR, file=STDERR)
    return key


def input_method() -> int:
    """Ask the user for the input method (File or Console).


    Returns
    -------
    int - Input method chosen (0 - File | 1 - Console)

    """
    while True:
        print("\n-- Input method --\n0 - File | 1 - Console")
        in_method = int(input())
        if in_method in {0, 1}:
            break
        print(INPUT_ERROR, file=STDERR)
    return in_method


def output_method() -> int:
    """Ask the user for the output method (File or Console).


    Returns
    -------
    int - Output method choen (0 - File | 1 - Console)

    """
    while True:
        print("\n-- Output method --\n0 - File | 1 - Console")
        out_method = int(input())
        if out_method in {0, 1}:
            break
        print(OUTPUT_ERROR, file=STDERR)
    return out_method
