from operations_functions.a_merge_b import merge_a_b
from operations_functions.a_intersection_b import intersection_a_b
from operations_functions.a_difference_b import difference_a_b
from operations_functions.a_symmetrical_difference_b import symmetrical_difference_a_b


def get_result(a, b):
    res_merge_a_b = merge_a_b(a, b)
    res_intersection_a_b = intersection_a_b(a, b)
    res_difference_a_b = difference_a_b(a, b)
    res_symm_diff_a_b = symmetrical_difference_a_b(a, b)

    res_merge_a_b = ', '.join(str(x) for x in res_merge_a_b)
    res_intersection_a_b = ', '.join(str(x) for x in res_intersection_a_b)
    res_difference_a_b = ', '.join(str(x) for x in res_difference_a_b)
    res_symm_diff_a_b = ', '.join(str(x) for x in res_symm_diff_a_b)

    return res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b
