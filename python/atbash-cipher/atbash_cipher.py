import string


def encode(plain_text):
    plain_text = ''.join(e for e in plain_text if e.isalnum()).lower()
    intab = string.ascii_lowercase
    outtab = intab[::-1]
    ciphered_text = plain_text.translate(str.maketrans(intab, outtab))
    ciphered_text = [ciphered_text[i: i+5] for i in range(0, len(plain_text), 5)]
    return (' '.join(ciphered_text))


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(' ', '')
    outtab = string.ascii_lowercase
    intab = outtab[::-1]
    plain_text = ciphered_text.translate(str.maketrans(intab, outtab))
    return plain_text


"""
Better solution:

from string import (
    ascii_letters,
    ascii_lowercase as low,
    ascii_uppercase as up,
)
from itertools import chain


REVERSED = ''.join(chain(reversed(low), reversed(up)))
TABLE = str.maketrans(ascii_letters, REVERSED)


def encode(plain_text):
    encoded = ''.join(a for a in plain_text.translate(TABLE).lower() if a.isalnum())
    return " ".join(encoded[x:x+5] for x in range(0, len(encoded)+1, 5)).strip()


def decode(ciphered_text):
    return ciphered_text.replace(' ', '').translate(TABLE)

"""
