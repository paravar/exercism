def detect_anagrams(word, candidates):
    for c in candidates:
        if c.lower() == word.lower():
            candidates.remove(c)
    anagram = []
    word_list = sorted(list(word.lower()))
    for c in candidates:
        cand_list = sorted(list(c.lower()))
        if cand_list == word_list:
            anagram.append(c)
    return(anagram)


"""
better way:

def detect_anagrams(word, candidates):
    l = []
    w = list(word.lower())
    w.sort()
    for c in candidates:
        a = list(c.lower())
        a.sort()
        if a == w and c.lower() != word.lower():
            l.append(c)
    return l
"""
