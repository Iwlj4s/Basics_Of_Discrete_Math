# Data For Index.html #
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

# Data For Complement.html #
complement_data ={
    'example_about_operation1': 'U = {1, 2, 3, 4, 5, 6, 7, 8, 9} ',
    'example_about_operation2': 'X =  {1, 2, 3, 4}',
    'operations': [
        {
            'operation_name': 'Complement',
            'operation_info': 'Write the elements of the set U by removing elements from set X',
            'res_example': 'X′ = { 1, 2, 3, 4, 5, 6 }'
        }]
}