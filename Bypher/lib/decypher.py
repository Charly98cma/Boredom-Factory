from lib import io, err_msgs

def decypher(in_method: int, perm_len: int, letter_len: int) -> str:
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
    raw_text = io.read_text(in_method, perm_len)
    ptr_1 = 0
    for ptr_2 in range(perm_len*letter_len, len(raw_text)+1,
                       perm_len*letter_len):
        for i in range(perm_len):
            clear_txt += chr(int(raw_text[ptr_1:ptr_2][i::perm_len], 2))
            ptr_1 = ptr_2
        print(clear_txt)
    return clear_txt
