from itertools import chain
from lib import io, err_msgs


def sliding_window(raw_text: str, perm_len: int) -> list[list[str]]:
    """Create a list of lists of each permutation group.


    Parameters
    ----------
    raw_text: str - Text to cypher/decypher
    perm_len:int - Length of permutations group (1st key)


    Returns
    -------
    list[list[str]] - List of permutations groups (lists)

    """
    return [raw_text[i:i+perm_len]
            for i in range(0, len(raw_text), perm_len)]


def turn_to_binary(text_groups: list[list[str]], bin_format: str) -> list[list[str]]:
    """Create a list of lists with eahc permutation group on binary format.


    Parameters
    ----------
    text_groups: list[list[str]] - Permutations groups on 2D lists
    bin_format: str - Binary format to use for each character


    Returns
    -------
    list[list[str]] - List of permutations groups (list) of each part on binary format

    """
    return [[bin_format.format(ord(a)) for a in b] for b in text_groups]


def cypher(in_method: int, perm_len: int, bin_format: str) -> str:
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
    raw_text = io.read_text(in_method, perm_len)
    for block in turn_to_binary(
            sliding_window(raw_text, perm_len),
            bin_format):
        coded_text += ''.join(list(chain.from_iterable(zip(*block))))
    return coded_text
