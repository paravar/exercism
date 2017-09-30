def to_rna(foo):
    for x in foo:
        if x not in "GCTA":
            return ""
    bar = str.maketrans("GCTA", "CGAU")
    return foo.translate(bar)
