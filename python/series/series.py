"""
def slices(series, length):
    if length > len(series) or length == 0:
        raise ValueError
    series_list = list(series)
    new_list = []
    i, c = 0, length
    while i <= len(series) - length:
        new_list.append(list(map(int, series_list[i:c])))
        i, c = i + 1, c + 1
    return new_list
"""

"""
def slices(series, length):
    if length == 0 or length > len(series):
        raise ValueError("invalid length")
    return [[int(c) for c in series[i:i+length]] for i in range(0, len(series)-length+1)]
"""


def slices(series, length):
    if length > len(series) or length == 0:
        raise ValueError
    return [list(map(int, series[i:i+length])) for i in range(0, len(series) -
            length + 1)]
