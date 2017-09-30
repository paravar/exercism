def to_rna(dna):
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    dna = list(dna)
    for s in range(len(dna)):
        try:
            dna[s] = dna_to_rna[dna[s]]
        except:
            dna = ''
            break
    return(''.join(dna))
