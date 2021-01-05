def complement_dna(dna):
    """
    Complementing a Strand of DNA

    In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

    The reverse complement of a DNA string s is the string sc formed by reversing
    the symbols of s, then taking the complement of each symbol (e.g., the reverse
    complement of "GTCA" is "TGAC").

    Parameters
    ----------
    dna

    Returns
    -------
    The reverse complement of the DNA
    """
    result = dna[::-1]

    result = result.replace('A', 'X')
    result = result.replace('T', 'A')
    result = result.replace('X', 'T')

    result = result.replace('C', 'X')
    result = result.replace('G', 'C')
    result = result.replace('X', 'G')

    return result


if __name__ == '__main__':
    string = 'GCGTCTGCGTCCAATTAACGAAGTTAACCGGGTACCCACTGAATGTGGTTAACCGGTGTTGCTTTCGAAGCAGTTGTTTTAACTCGGCGTTGCTAATAAAGGAGGTCCTTAATGGGATTACCAGTTCACGTACTGAGCGGTATGTTGGCTGGAACAGCAGTTAAGTCTGCCACCCTTGGCACCCCATCTATTGTTACTACACATGTGATTACAAGACGGAAGCCGGTTTTAGTCATTATGTCACGGTTCCGGGATACGCATCCAGAGGTACTCGTCCCTAAAAACGACAAGGAGAGTAACGATGCATCATCCACACTAACTGAGGGTCGCGTGTTAACCGCCCGGAGCATAATTCGCAATTACAAGTCTGACGAACAGTATAAAAATGCTCGGTGGTAGCCTCTTCGTTTCGGGGGAGGATCCCTTCCTTGTGACTAATCAAGCTGAATCTCATGTACCTGAGTAAAACATGCGTCCAATATAATGACGCAGGCTTCTATCCCTTTCGTTGGGTACCCTAACTTTTGTGCTATTCGCGGTGGTCCGTCTGTTCATGCTAGCATGAACGGCGAAATACAGACGTAAGATTGGGCAAACCATAACGTAGGCAGCGGATCTTACAGGGCTTTCATGGTATTGCTTAATGTGAGGGTCGCCAGCTGGCCGTCATCGCCGCGCAGAATAACGTAGCTAGCGGCAGGCCACATACGTGCCAGCAAGGAAGCGTGACGTTTTGTTATAACAAGCCTATCTGCGCTCCACCTATCAGCAATTCTATCAGGCGACTAATTTTACCGGCTCATAGGTGGCGTAACAAAGGACACCTACCGAGCAGGGAGCAGACACCCTAAGTGGCGTGGATATGGTGTCCTCGGGAT'
    print(complement_dna(string))