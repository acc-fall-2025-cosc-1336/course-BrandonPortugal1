def get_p_distance(list1, list2):
    """
    Compute the p-distance between two DNA lists.
    p-distance = (# differing positions) / (length of sequence)
    """
    differences = 0
    length = len(list1)

    for i in range(length):
        if list1[i] != list2[i]:
            differences += 1

    return differences / length


def get_p_distance_matrix(dna_lists):
    """
    Compute the full p-distance matrix for a list of DNA lists.
    """
    n = len(dna_lists)
    p_distance_matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(get_p_distance(dna_lists[i], dna_lists[j]))
        p_distance_matrix.append(row)

    return p_distance_matrix