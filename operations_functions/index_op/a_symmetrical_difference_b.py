from operations_functions.index_op.a_merge_b import merge_a_b

from operations_functions.index_op.a_intersection_b import intersection_a_b


def symmetrical_difference_a_b(a, b):
    a_symmetrical_difference_b = []

    merge = merge_a_b(a, b)
    intersection = intersection_a_b(a, b)

    for i in merge:
        if i not in intersection and i not in a_symmetrical_difference_b:
            a_symmetrical_difference_b.append(i)

    a_symmetrical_difference_b.sort(key=int)

    return a_symmetrical_difference_b

