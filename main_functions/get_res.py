from operations_functions.index_op.a_merge_b import merge_a_b
from operations_functions.index_op.a_intersection_b import intersection_a_b
from operations_functions.index_op.a_difference_b import difference_a_b
from operations_functions.index_op.a_symmetrical_difference_b import symmetrical_difference_a_b
from operations_functions.complement_op.complement import complement


# Get Result for INDEX.html page #
def get_index_result(a, b):
    res_merge_a_b = merge_a_b(a, b)
    res_intersection_a_b = intersection_a_b(a, b)
    res_difference_a_b = difference_a_b(a, b)
    res_symm_diff_a_b = symmetrical_difference_a_b(a, b)

    res_merge_a_b = ', '.join(str(x) for x in res_merge_a_b)
    res_intersection_a_b = ', '.join(str(x) for x in res_intersection_a_b)
    res_difference_a_b = ', '.join(str(x) for x in res_difference_a_b)
    res_symm_diff_a_b = ', '.join(str(x) for x in res_symm_diff_a_b)

    return res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b


# Get Result for COMPLEMENT.html page #
def get_complement_result(u, a):
    res_complement = complement(u, a)
    res_complement = ', '.join(str(x) for x in res_complement)

    return res_complement
