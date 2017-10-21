import string


def rotate(text, key):
    if key in [0, 26]:
        return(text)
    Ucase_latters = string.ascii_uppercase
    Lcase_letters = string.ascii_lowercase
    original_letters = Lcase_letters + Ucase_latters
    Ucase_dic = []
    Lcase_dic = []
    for c in Ucase_latters:
        Ucase_dic.append(Ucase_latters[Ucase_latters.index(c) - (26 - key)])
        Lcase_dic.append(Lcase_letters[Lcase_letters.index(c.lower()) - (26 - key)])
    Ucase_dic = ''.join(Ucase_dic)
    Lcase_dic = ''.join(Lcase_dic)
    dic = Lcase_dic + Ucase_dic
    transtab = string.maketrans(original_letters, dic)
    return(text.translate(transtab))
