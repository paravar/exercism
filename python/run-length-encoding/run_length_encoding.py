def encode(string):
    if len(string) in [0, 1]:
        return(string)
    prev = ''
    count = 1
    lst = []
    for character in string:
        if character != prev:
            if prev:
                if count == 1:
                    lst.append(prev)
                    prev = character
                    count = 1
                else:
                    lst.append(str(count))
                    lst.append(prev)
                    prev = character
                    count = 1
            else:
                count = 1
                prev = character
        else:
            count += 1
    else:
        if count == 1:
                    lst.append(prev)
        else:
            lst.append(str(count))
            lst.append(character)
    return(''.join(lst))


def decode(string):
    if len(string) in [0, 1]:
        return(string)
    mult = ''
    result = ''
    for i in string:
        if i.isdigit():
            mult += str(i)
        else:
            if mult:
                result += int(mult) * i
                mult = ''
            else:
                result += i
    return(result)
