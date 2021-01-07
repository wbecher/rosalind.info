def load_fasta(filename):
    """
    Open a fasta txt file and returns a formatted dict.

    Parameters
    ----------
    filename

    Returns
    -------
    A Formatted dict where the keys are the labels, and the values are the DNA strings.
    """
    # open file
    with open(filename, "r") as arquivo:
        texto = arquivo.readlines()

    # create empty dict
    fasta = dict()
    for linha in texto:
        linha = linha.strip().strip('\n')
        if not linha:
            continue
        if linha.startswith('>'):
            label = linha[1:]
            if label not in fasta.keys():
                fasta[label] = []
                continue
        sequence = linha
        fasta[label].append(sequence)

    for chave in fasta.keys():
        fasta[chave] = ''.join(fasta[chave])

    return fasta


if __name__ == '__main__':
    pass
