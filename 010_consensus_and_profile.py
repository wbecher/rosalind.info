import numpy as np

letras = {
    0: 'A',
    1: 'G',
    2: 'C',
    3: 'T'
}


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


def consensus(m):
    largura = m.shape[1]
    consenso = np.zeros(largura)
    contagem = np.zeros((4, largura))
    for letter in range(largura):
        linha = m[:, letter]
        linha = ''.join(linha)
        a = linha.count('A')
        g = linha.count('G')
        c = linha.count('C')
        t = linha.count('T')
        contagem[0, letter] = a
        contagem[1, letter] = g
        contagem[2, letter] = c
        contagem[3, letter] = t

    for d in range(largura):
        consenso[d] = contagem[:, d].argmax()

    consenso = ''.join([letras[p] for p in consenso])
    print(consenso)

    for id, linha in enumerate(list(contagem)):
        print(f'{letras[id]}:', ' '.join([str(x).replace('.0', '') for x in linha]))


def create_matrix(args: list):
    linhas = []
    for i, x in enumerate(args):
        linha = []
        for y in x:
            linha.append(y)
        linhas.append(linha)

    matrix = np.array(linhas)

    return matrix


if __name__ == '__main__':
    strings = load_fasta('consensus_and_profile.txt').values()

    m = create_matrix(strings)
    consensus(m)
