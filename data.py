# Data For INDEX.html #
index_data = {
    'example_about_operation1': 'A = { 1, 2, 3, 4 }',
    'example_about_operation2': 'B = { 3, 4, 5, 6 }',
    'operations': [
        {
            'operation_name': 'Merge',
            'operation_info': 'Write the elements of the set A and B in ascending order; if an element occurs >1 '
                              'time, write it once',
            'res_example': 'A ⋃ B = { 1, 2, 3, 4, 5, 6 }'
        },
        {
            'operation_name': 'Intersection',
            'operation_info': 'Write out identical elements from A and B',
            'res_example': 'A ⋂ B = { 3, 4 }'
        },
        {
            'operation_name': 'Difference',
            'operation_info': 'A \ B - Rewrite A, removing elements that are in B',
            'res_example': 'A \ B = { 1, 2 }',
            'operation_info2': 'B \ A - Rewrite B, removing elements that are in B',
            'res_example2': 'B \ A = { 5, 6 }'
        },
        {
            'operation_name': 'Symmetrical Difference',
            'operation_info': 'Write out elements from A ⋃ B, removing elements from A ⋂ B',
            'res_example': 'A △ B = { 1, 2, 5, 6}'
        },
    ]
}

# Data For COMPLEMENT.html #
complement_data = {
    'example_about_operation1': 'U = {1, 2, 3, 4, 5, 6, 7, 8, 9} ',
    'example_about_operation2': 'X =  {1, 2, 3, 4}',
    'operations': [
        {
            'operation_name': 'Complement',
            'operation_info': 'Write the elements of the set U by removing elements from set X   ( X can be A′ or B′ )',
            'res_example': 'X′ = { 5, 6, 7, 8, 9}'
        }]
}

# Data For number_PERMUTATION.html #
find_number_permutation_data = {
    'operations': [
        {
            'operation_name': 'Calculating the number of permutations of n elements',
            'operation_info': 'The number of permutations Pn is the number of different ways in which a given set '
                              'consisting of n elements can be ordered. ',
            'res_example': 'P_n = n! = P₁₀ = 10! = 3628800'
        },]
}

# Data For number_PLACEMENTS.html #
find_number_placements_data = {
    'operations': [
        {
            'operation_name': 'Calculating the number of placements of n by k elements',
            'operation_info': 'The number of placements of Ank is the arrangement of “items” on some “places”, '
                              'provided that each place is occupied by exactly one object and all objects are '
                              'different. More formally, an arrangement (from n to k) is an ordered set of k distinct '
                              'elements of some n-element set.',
            'res_example': 'A_9^2 = 9!/(9-2)! = 9!/7! = 72 '
        },]
}

# Data For number_COMBINATIONS.html #
find_number_combinations_data = {
    'operations': [
        {
            'operation_name': 'Calculating the number of combinations of n by k elements',
            'operation_info': 'The number of combinations from n to k (C_n^k) is a set of k elements selected from '
                              'given n elements. Sets that differ only in the order of elements (but not in '
                              'composition) are considered identical.',
            'res_example': 'C_9^2 = 9!/(9-2)! * 2! = 9!/7! * 2! = 36 '
        },]
}
