import random
from string import ascii_letters


def get_string(l: int):
    chars = ascii_letters
    res = ''
    for i in range(l):
        res += chars[random.randint(0, len(chars)-1)]
    return res
