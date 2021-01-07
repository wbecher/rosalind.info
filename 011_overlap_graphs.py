from helpers import load_fasta


def find_overlaps(fasta):
    links_dict = {}

    for cod in fasta.keys():
        links_dict[cod] = []
        origem = fasta[cod]
        for chave in fasta.keys():
            compara = fasta[chave]
            if not(cod == chave):
                prefixo = compara[:3]
                sufixo = origem[-3:]
                if sufixo == prefixo:
                    links_dict[cod].append(chave)

    return links_dict


if __name__ == '__main__':
    file = load_fasta('overlap_graph.txt')
    links = find_overlaps(file)

    for id1 in links.keys():
        if links[id1]:
            for id2 in links[id1]:
                print(id1, id2)
