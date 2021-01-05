from scipy.special import comb

hom = 2
het = 2
rec = 2


def mendel(hom, het, rec):
    """
    Three positive integers k, m, and n, representing a population containing
    k+m+n organisms: k individuals are homozygous dominant for a factor, m
    are heterozygous, and n are homozygous recessive.

    Parameters
    ----------
    hom: int
    het: int
    rec: int

    Returns
    -------
    The probability that two randomly selected mating organisms will produce an
    individual possessing a dominant allele (and thus displaying the dominant
    phenotype). Assume that any two organisms can mate.
    """
    pop_total = 4 * comb(hom + het + rec, 2)
    rec_total = 4 * comb(rec, 2) + 2 * rec * het + comb(het, 2)
    prec = rec_total / pop_total
    probability = 1 - prec
    return probability


if __name__ == '__main__':
    a, b, c = 25, 18, 30
    print(mendel(a, b, c))
