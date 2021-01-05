def count_dna_nucleotides(dna):
    """
    http://rosalind.info/problems/dna/

    Receives a DNA string and returns the count of times that the symbols
    'A', 'C', 'G', and 'T' occur in.

    Parameters
    ----------
    dna

    Returns
    -------
    A String with Four integers (separated by spaces) counting the respective
    number of times that the symbols 'A', 'C', 'G', and 'T' occur in.
    """
    a = dna.count('A')
    c = dna.count('C')
    g = dna.count('G')
    t = dna.count('T')
    return f'{a} {c} {g} {t}'


if __name__ == '__main__':
    string = 'ATACGTCCACCGGGGAGGGCATAGTGCGCAGCCGGAGAGATTTATAACAGGTCGCAAATTTGTGCAGAGTCCCTATTAGCGTAGCCGCTGCCGGGTCTTTGACGAAAGCGACAAAGTCGTAGTTGTGTGCCTTGATCCACTAGCAACGCAGATACATCTTGGTCGTCAAGGACCCTTAGGAGTTGAAGCTTTGATTGCCGCAGGATTCCTTGCTAACCGTTGATGGGAATTGGTGTCCGGACGTCAGATTTCGATAAAGGTCCTGACATCAGGTCCCATGACTAACTCCGGGACAGCTTGCCGGCGGGCGATACTCGCGCTCATTGCGCGATGTTAACCTCTGAGTCCCCCGAATCTTAACGCGCGGCCAAACATCATAACAATTCCGCTTCCGTAGGTTCCCGATGCTAGCCGCGACCCATCATAACCTCATTTCTGACGTATTTCCCTTACTGACTCAACCGCTCTACAAGTTTACTAATCTGGGTAGTTAACGGTCTCGGAGTGCACACCATTTTAAGAGATACGAAAATGATTAATACAGCGCGGCGGGGCACACGTTCTGGAAGGTGTCATAAGTGTTCCCACCGTTGCCGGAGGAAGCCAAATGCACAGGAATGCGTCTGGACTCCCGCACGCCTGGGTAAACCCCCGCACGTCCACTCGCGCTGAGTCACCTCGATCGTGTTAGATCCTGCACTCTACTTTACTCGGTGATTATGACTTATCCCCGCTGCGAGGCAAACTCAACCCGGCTCGTCTTAGTCAGGACTCGGGACGTATCCGGGATTAACAGACAAGGGTGGTGTCCAATCACATTTCCGATCGTAGTGGACTTCGGGTCAGTTTCTTAACTCGATCTGGGTGGTATTGCCTTACTAGGGCTCCGC'
    print(count_dna_nucleotides(string))
