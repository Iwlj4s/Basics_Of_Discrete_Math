def complement(u, a):
    res_u_complement_a = []

    for i in range(len(u)):
        if u[i] not in a and u[i] not in res_u_complement_a:
            res_u_complement_a.append(u[i])

    return res_u_complement_a

