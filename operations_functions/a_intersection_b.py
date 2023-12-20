def intersection_a_b(a, b):
    a_intersection_b = []

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and a[i] not in a_intersection_b:
                a_intersection_b.append(a[i])
            a_intersection_b.sort(key=int)

    return a_intersection_b
