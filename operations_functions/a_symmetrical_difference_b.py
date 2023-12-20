def symmetrical_difference_a_b(a, b):
    a_symmetrical_difference_b = []

    for i in range(len(a)):
        if a[i] not in b and a[i] not in a_symmetrical_difference_b:
            a_symmetrical_difference_b.append(a[i])

    for j in range(len(b)):
        if b[j] not in a and b[j] not in a_symmetrical_difference_b:
            a_symmetrical_difference_b.append(b[j])
        a_symmetrical_difference_b.sort(key=int)

    return a_symmetrical_difference_b

