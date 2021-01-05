def dna_to_rna(dna):
    """
    Transcribing DNA into RNA

    Given a DNA string corresponding to a coding strand, its transcribed RNA
    string is formed by replacing all occurrences of 'T' in with 'U'.

    Parameters
    ----------
    String dna

    Returns
    -------
    Return: The transcribed RNA string.
    """
    return dna.replace('T', 'U')


if __name__ == '__main__':
    string = 'GGCAGAACATTAATCCGCCTGTATCGGACCCGGCAAGTTGCACGTTAATCGAGGTAAAACTACTCGTTCCGGGTAGAAAGCGAAGCACCTCTTGAGGAATATAGTCACTGAAGCCAGCAAAATGAACGGACCTGTAGGTAGTGGCGCTCATATCATTCTAGGGTGGTTCCATACTTGCCTATAGTTATCTCCCCGAAAATAGCTATCGCGACGCTGCCATTCCCGATCAACTACCCCAACTCTGAGATTTATCGCTCTCTCTTACTTGTTTGCACTTCGACCGGTCGCACAATCGTGAAGGGCGGCGCTCAGCCCTTTTGAGTATTCGAGAATCAGATAGGTCTACAATATCCCTTGTGTGCACTGCCAGAGGCCCTACCAACTGCTGCTTGAACTAGCCTTTGATCGGCTATCTCCCTGTGAGCATGCATTTAAAGGGTTTCCAATCCGGCGAACAGTGACCTGAGTGAGCCGTTTGTAAAAGGAGGTGAGGTCAGCTAGATCAACGTGAAGCTCAGCATTGCCACTGCGGCAAGAATCTACACTGAAAAAGAAGATGGGCTGCGCCCTCCCGGCGCCCTCCCTGGCGAATTCAGAACGGGATCAAATATGAGTCTGTCGTACTTGCTAGGTGTTCGCAAGTTTTATTCCATGAGCAACAGACATCCCCGGCCCGTACCAAACGGCGGACCTGATAAATATAGCACAATAACAGCGGCGAATGCATATGAGATAGAAATCTAGCCCACCCCAGGATACCAGGTTATCACAAAGTGCGGCCCATGCGATAGGGTTGGCGCACCTCAGGTGAAAAGAGTGGTAGAATGTATGGGTACTTGGTCCCTAGGTAGGCACCTTCCAATTGATCATCTCAGCGATGAAGTTGCACAACACGCGGCTCCAGCGACTCCGCGTCAGATAAAGGCTATACAGAAGCACGCTCAG'
    print(dna_to_rna(string))