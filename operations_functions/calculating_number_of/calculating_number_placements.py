from math import factorial


def placements(n, k):
    res_placements = []

    A = factorial(n) / factorial((n-k))

    res_placements.append(A)

    return res_placements
