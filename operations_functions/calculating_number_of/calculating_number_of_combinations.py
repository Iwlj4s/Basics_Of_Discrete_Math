from math import factorial


def combinations(n, k):
    res_combinations = []
    a = factorial(n)
    b = factorial((n - k))
    z = b * factorial(k)

    C = a / z

    res_combinations.append(C)

    return res_combinations
