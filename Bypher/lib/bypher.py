#!/usr/bin/env python3
from sys import exit, stderr as STDERR
from lib import ask, io, cypher, decypher



def main():
    """Byphers' main function."""
    try:
        op = ask.operation()
        # key_l[0] = len of permutation groups
        # key_l[1] = len of representation
        key_l = ask.key()
        in_method = ask.input_method()
        out_method = ask.output_method()
        if op == 0:
            new_txt = cypher.cypher(
                in_method, key_l[0], "{"+f"0:0{key_l[1]}"+"b}")
        elif op == 1:
            new_txt = decypher.decypher(
                in_method, key_l[0], key_l[1])
        else:
            print("*** Operation not supported ***", file=STDERR)
            exit(1)
        io.print_result(new_txt, out_method)
    except (TypeError, ValueError):
        print("*** You can't do that :P **", file=STDERR)
        exit(-1)
    except KeyboardInterrupt:
        exit(-1)
    exit(0)


if __name__ == "__main__":
    main()
