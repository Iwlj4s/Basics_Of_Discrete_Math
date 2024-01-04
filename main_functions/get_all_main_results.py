from main_functions.get_res import get_index_result, get_complement_result
from main_functions.checking_user import check_user_data, check_user_digit

import inspect


# FULL CHECK AND RETURN RESULT #
def full_checked_results(x, y, x_value, y_value):
    # Check Caller Function #
    caller = inspect.currentframe().f_back.f_code.co_name

    # Check user enter is not nothing
    check_user_enter = check_user_data(a=x, b=y)

    # Replace , and spaces for check user entry digit
    check_user_enter_digit = check_user_digit(a=x.replace(',', '').replace(' ', ''),
                                              b=y.replace(',', '').replace(' ', ''))

    if check_user_enter_digit:
        if not check_user_enter:
            # If user Input digit
            a = x.replace(',', '').split()  # Get User Input Value
            b = y.replace(',', '').split()

            # Get Result
            # caller INDEX #
            if caller == 'index':
                res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b = get_index_result(a, b)

                return res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b, x_value, y_value

            # caller COMPLEMENT #
            if caller == 'complement':
                res_complement = get_complement_result(a, b)

                return res_complement, x_value, y_value

        elif check_user_enter:
            x_value = "You should enter sets"
            y_value = "You should enter sets"

            # caller INDEX #
            if caller == 'index':
                return "", "", "", "", x_value, y_value

            # caller COMPLEMENT #
            if caller == 'complement':
                return "", x_value, y_value

    else:  # If User input string
        x_value = "You should enter digit"
        y_value = "You should enter digit"

        # caller INDEX #
        if caller == 'index':
            return "", "", "", "", x_value, y_value

        # caller COMPLEMENT #
        if caller == 'complement':
            return "", x_value, y_value
