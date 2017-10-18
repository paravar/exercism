import string

"""
def hey(bob_string):
    strip_string = (string.whitespace + string.punctuation).replace('?', '')
    bob_string = bob_string.translate(None, strip_string)
    if bob_string.isupper():
        return"Whoa, chill out!"
    elif bob_string == "":
        return"Fine. Be that way!"
    elif bob_string[len(bob_string) - 1] == '?':
        return"Sure."
    else:
        return"Whatever."
"""


def hey(phrase):
    phrase = phrase.strip()
    if not phrase:
        return 'Fine. Be that way!'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
