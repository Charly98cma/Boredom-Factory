#!/usr/bin/env python3
from sys import exit, stderr as STDERR
from lib import ask, io, cypher, decypher


def __cypher(method, group_len, resp_len):
    return cypher.cypher(method, group_len, "{"+f"0:0{resp_len}"+"b}")


def __decypher(method, group_len, resp_len):
    return decypher.decypher(method, group_len, resp_len)


OPERATIONS = {
    0: __cypher,
    1: __decypher
}


def main():
    """Byphers' main function."""
    try:
        op = ask.operation()
        # key_l[0] = len of permutation groups
        # key_l[1] = len of representation
        key_l = ask.key()
        in_method = ask.input_method()
        out_method = ask.output_method()
        new_txt = OPERATIONS[op](in_method, key_l[0], key_l[1])
        io.print_result(new_txt, out_method)
        exit(0)
    except KeyboardInterrupt:
        exit(-1)
    except KeyError:
        print("*** Operation not supported ***", file=STDERR)
        exit(-2)
    except (TypeError, ValueError):
        print("*** You can't do that >:( ***", file=STDERR)
        exit(-3)

if __name__ == "__main__":
    main()
