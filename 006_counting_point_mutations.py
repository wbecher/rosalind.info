def count_point_mutations(s, t):
    """
    Counting Point Mutations

    Given two strings s and t of equal length, the Hamming distance between s
    and t, denoted dH(s,t), is the number of corresponding symbols that
    differ in s and t

    Parameters
    ----------
    dna1: str
    dna2: str

    Returns
    -------
    An integer, equals to the Hamming distance dH(s,t).
    """
    mutations = sum([1 for x in zip(s, t) if x[0] != x[1]])
    return mutations


if __name__ == '__main__':
    string1 = 'CGACGTCAAAACGATATTGCACTTGCTAGCTCACCTCAATCTCCATGACAGTAACTTCCATATCGCAGTACCGGCCAGGCTGCGACTTTGCGGGCTTCAAGCCCAGGTCGCCCTATACTCGCGCTTGGCTGTTTTTTACCCACGGTCCTGAGGAAGTGTGGCACCGAGAGATCTTGGTCGAGACAGGTACCCCAGGGATCGTGTGACCGGGCATTCCTTTAGTCGTAGACTATGTTCATAGCATCGGCCAATTGTTCGGCTGTGAGACTCTTGCAATGGGAATCGCCCAAAGCGGGTAGTTCGACCGATAAAGACCGCGTTAGTATCGCGCAAGCTATGTAGAGGGACTTGCGTCCTCGCGGCACAAAATTTCACATTTCGCTGCTTTGCCCACCAGTTTGTTTCGACCTGGGCCAAAGCGGTACTATTTAGACTGAGAATCACTTCACCATACCTACAACGAGCAATCCAGGTATACAGGACCTCAAAGGTGAGCGCCGCACACATCGTGGGCGGTCGACCAATCTTTTGCACCCCTGGTCAATGCACTTCCTAGTTGCTGCACGGCTCAAGGCCGTAAACGCCGCAAAACAGAAGCACGATCGCCACACATAAGCCGCAACCAGATCTCTTGAGGTACTACCTACGACTATCGAAGACAGATCTATGAGCCTCTGAAAATCGAGACAAGGGCATTCCTATCACTACCTAGGTAGGCTGCGAATGGGAGAAGAGGGGGACTTTTCCAAAGGTTAATCAAAAAGTCACGCAAAGAATCCGAAGGTTTAAGCCACCACCTTGCAAGGACGAACTCGATAAACAGCGGGAGCATCAAAATGCACTCCGCCCTCGCACACAGAGGCCGTTGCCAATCATCCCGCAAACAGGCCTGGCGTTAGCGTCGGTCGATACCCGATATCGTTGGAC'
    string2 = 'CCCCCGCTGTACTCGATTCGTCTCTCGAAGTAGCCGGAATCGTCATGGCCGTGAGTGCGAGATACGCGTAGGGAGCAGTCAGTGAATTCGCGGGCTTCTAACGTAGTAAGATGTTGGATCACCGTTTTCCTTTTGTGCCATCGCTCCATGTTGATGTTCGAGAATGGGACCTGCTGACAGTGTACGGGTCTCTCAGACTTCTGTGATCTGGCATTCAATCAGTAGTACACTGTTGTCAAGGCATGGGCCAGATGTTTCGCTGGGTTTCGGGCGCTATGAAATTTCACCAGCAGTGCGAGTAGAAGGTATTATCACATGGCTATGCTGGCGGGTGCTCTTAGTGGGGATTTGTGTCGAGGCGATGCCCCGTGTTAAATAGGCCGATTCTGGCAGCCCGACGATTCTCGACTAGACTAAAGCTGGCCTATTTCATCGGCCAACAGTTCCCCTGTAGCAAATGCGAGTATGCGCAATACTCTGTACCCAAAAGAAGCTCGTCTCACACCCCGCGTGGTTGCGGGCAATCTTGCATACCCCTTCCCACTCAGCTCACGATTAACTGCAAGGTAGACGGTTATTTAATTCACAATGGTGAAGCGCGATCAGCACCTAGAAGGTGACCCTAACTGTCATGAATTACTATGCGCCATGGACAGAACCGTACCTATGGGCCTATAAGGGGCGATGTCTAGCAATTCCTAATACTAACCATGTAGAATCCGACCGTGAAGAGTTGTGCAAGCTTCCGGGTAAAAACCTAACGCACACTTATGAATTATGAACCATGAAGTGACGACGTTGCCATCCGCAACTCGATTCTCAACCTGCTCTTCACACGCGACCACGCTCCCACACCGTGCGGGTGCCTCACACTGGACCGAAAGCAGGCAGGTGGTGAGCGTCGTGCCATATCAGATCTAGATATAC'

    result = count_point_mutations(string1, string2)

    print(result)
