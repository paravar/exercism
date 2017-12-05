def abbreviate(words):
    words = words.replace('-', ' ')
    acr = ''
    for word in words.split(' '):
        acr += word[0].upper()
    return acr


"""
Better solution:

import re


def abbreviate(words):
    word_list = re.split(r'\W+', words)
    acronym = ''.join([w[0] for w in word_list])
    return acronym.upper()

"""
