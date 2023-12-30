def merge_a_b(a, b):
    res_a_merge_b = []

    for i in range(len(a)):
        if a[i] not in b and a[i] not in res_a_merge_b:
            res_a_merge_b.append(a[i])

    for j in range(len(b)):
        if b[j] not in res_a_merge_b:
            res_a_merge_b.append(b[j])

    res_a_merge_b.sort(key=int)

    return res_a_merge_b
