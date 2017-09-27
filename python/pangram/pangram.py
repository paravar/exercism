import string


def is_pangram(s):
    return set(s.lower()) >= set(string.ascii_lowercase)
