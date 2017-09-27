def is_isogram(string):
    lower = string.lower()
    visited = set()
    for c in lower:
        if not c.isalpha():
            continue
        if c in visited:
            print("\"%s\" is not an isogram.") % (string)
            return False
        else:
            visited.add(c)
    print("\"%s\" is an isogram!") % (string)
    return True
