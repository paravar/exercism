import string
import re


def word_count(text):
    text = text.lower()
    for char in (string.punctuation + '\t' + '\n'):
        text = text.replace(char, ' ')
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    text = text.split(' ')
    count = {}
    for word in text:
        count[word] = count.get(word, 0) + 1
    return count
