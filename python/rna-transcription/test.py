dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
dna = 'GCT'
for s in range(3):
    dna = dna.replace(dna[s], dna_to_rna[dna[s]])

print(dna)
