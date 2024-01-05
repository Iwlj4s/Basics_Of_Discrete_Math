from operations_functions.index_op.a_merge_b import merge_a_b
from operations_functions.index_op.a_intersection_b import intersection_a_b
from operations_functions.index_op.a_difference_b import difference_a_b
from operations_functions.index_op.a_symmetrical_difference_b import symmetrical_difference_a_b

from operations_functions.complement_op.complement import complement

from operations_functions.calculating_number_of.calculating_number_of_permutations import permutations
from operations_functions.calculating_number_of.calculating_number_placements import placements
from operations_functions.calculating_number_of.calculating_number_of_combinations import combinations


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


# Get Result for NUMBER_PERMUTATIONS.html #
def get_permutations_result(n):
    n = int(n)
    res_permutations = permutations(n)
    res_permutations = ', '.join(str(x) for x in res_permutations)

    return res_permutations


# Get Result for NUMBER_PLACEMENTS.html #
def get_placements_result(n, k):
    res_placements = placements(n, k)
    res_placements = ', '.join(str(x) for x in res_placements)

    return res_placements


# Get Result for NUMBER_COMBINATIONS.html #
def get_combinations_result(n, k):
    res_combinations = combinations(n, k)
    res_combinations = ', '.join(str(x) for x in res_combinations)

    return res_combinations
