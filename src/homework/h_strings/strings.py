def get_hamming_distance(dna1, dna2):
    # Ensure both strings are the same length
    if len(dna1) != len(dna2):
        return "Error: Strings must be of equal length."

    distance = 0
    i = 0
    while i < len(dna1):
        if dna1[i] != dna2[i]:
            distance += 1
        i += 1
    return distance


# Function to compute the DNA reverse complement
def get_dna_complement(dna):
    complement = ""
    i = len(dna) - 1  # Start from the end of the string

    while i >= 0:
        base = dna[i]
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
        else:
            return "Error: Invalid DNA base found."
        i -= 1

    return complement