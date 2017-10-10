def distance(dna1, dna2):
    hamming = 0
    if len(dna1) == 0 and len(dna2) == 0:
        return hamming
    if len(dna1) != len(dna2):
        raise ValueError
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming += 1
        else:
            continue
    return hamming
