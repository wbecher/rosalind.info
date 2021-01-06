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


def gc_counting(fasta_dict):
    """
    Parameters
    ----------
    fasta_dict: dict

    Returns
    -------
    A dict with the ids and GC_Content % of dna string.
    """

    gc_dict = dict()

    for key in fasta_dict:
        dna = fasta_dict[key]
        g = dna.count('G')
        c = dna.count('C')
        total = len(dna)
        gc = ((g+c)/total)*100
        gc_dict[key] = round(gc, 6)
    return gc_dict


if __name__ == '__main__':
    nome = 'nome'
    dna = 'ATCGATCGGCTAGCTATAGCTAGCTAG'
    fasta_file = load_fasta('gc_content.txt')
    results = gc_counting(fasta_file)
    label_maior_gc = (max(results, key=results.get))
    valor_maior_gc = results[label_maior_gc]
    print(label_maior_gc)
    print(valor_maior_gc)
