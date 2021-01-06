def rrr(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return rrr(n - 1, k) + k * rrr(n - 2, k)


if __name__ == '__main__':
    print(rrr(36, 4))
