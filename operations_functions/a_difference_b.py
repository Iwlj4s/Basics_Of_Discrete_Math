def difference_a_b(a, b):
    a_difference_b = []

    for i in range(len(a)):
        if a[i] not in b and b not in a_difference_b:
            a_difference_b.append(a[i])
        a_difference_b.sort(key=int)

    return a_difference_b
