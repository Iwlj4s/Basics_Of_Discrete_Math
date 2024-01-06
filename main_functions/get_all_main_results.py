# import RESULT #
from main_functions.get_res import get_index_result, get_complement_result, get_permutations_result
from main_functions.get_res import get_placements_result, get_combinations_result

# import CHECKS #
from main_functions.checking_user import check_user_data, check_user_digit, check_user_n_k, check_number_of_numbers

# import CHECKS for ONE NUMBER #
from main_functions.checking_user import check_user_data_for_one_number, check_user_digit_for_one_number
from main_functions.checking_user import check_number_of_numbers_for_one_number

# import OTHER #
import inspect


# FULL CHECK AND RETURN RESULT #
def full_checked_results(x, y, x_value, y_value):
    # Check Caller Function #
    caller = inspect.currentframe().f_back.f_code.co_name

    # Checking for how much is numbers #
    if x is not '' and y is not '':
        x = str(x)
        y = str(y)

        # Check user enter is not nothing
        check_user_enter = check_user_data(a=x, b=y)

        # Replace , and spaces for check user entry digit
        check_user_enter_digit = check_user_digit(a=x.replace(',', '').replace(' ', ''),
                                                  b=y.replace(',', '').replace(' ', ''))

    else:
        x = str(x)
        check_user_enter = check_user_data_for_one_number(x)
        check_user_enter_digit = check_user_digit_for_one_number(x)

    try:
        if check_user_enter_digit:
            if not check_user_enter:
                # If user Input digit

                a = x.replace(',', '').split()  # Get User Input Value
                b = y.replace(',', '').split()

                # Get Result #

                # caller INDEX #
                if caller == 'index':
                    res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b = get_index_result(a, b)

                    return res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b, x_value, y_value

                # caller COMPLEMENT #
                if caller == 'complement':
                    res_complement = get_complement_result(a, b)

                    return res_complement, x_value, y_value

                # caller PERMUTATIONS #
                if caller == 'number_permutations':
                    if check_number_of_numbers_for_one_number(a, b):  # If user Enter ONE number #
                        res_permutations = get_permutations_result(x)

                        return res_permutations, x_value, y_value

                    else:
                        # If user Enter > 1 number #
                        x_value = "You should enter ONE number"
                        y_value = "You should enter ONE number"

                        return "", x_value, y_value

                # caller PLACEMENTS #
                if caller == 'number_placements':

                    if check_number_of_numbers(a, b):  # If user Enter ONE number #
                        if check_user_n_k(a, b):  # If user's numbers == n >= k
                            x = int(x)
                            y = int(y)

                            res_placements = get_placements_result(x, y)

                            return res_placements, x_value, y_value

                        else:
                            # If user Enter > 1 number #
                            x_value = "N Should be > or == k"
                            y_value = "N Should be > or == k"

                            return "", x_value, y_value

                    else:
                        # If user's numbers == n < k
                        x_value = "You should enter ONE number"
                        y_value = "You should enter ONE number"

                        return "", x_value, y_value

                # caller COMBINATIONS #
                if caller == 'number_combinations':
                    if check_number_of_numbers(a, b):  # If user Enter ONE number #
                        if check_user_n_k(a, b):  # If user's numbers == n >= k
                            x = int(x)
                            y = int(y)
                            res_combinations = get_combinations_result(x, y)

                            return res_combinations, x_value, y_value

                        else:
                            # If user Enter > 1 number #
                            x_value = "N Should be > or == k"
                            y_value = "N Should be > or == k"

                            return "", x_value, y_value

                    else:
                        # If user's numbers == n < k
                        x_value = "You should enter ONE number"
                        y_value = "You should enter ONE number"

                        return "", x_value, y_value

            # If User input == digit or User input < 1
            elif check_user_enter:
                x_value = "You should enter sets"
                y_value = "You should enter sets"

                # caller INDEX #
                if caller == 'index':
                    return "", "", "", "", x_value, y_value

                # caller COMPLEMENT | PERMUTATIONS | PLACEMENTS | COMBINATIONS #
                if (caller == 'complement' or caller == 'number_permutations' or caller == 'number_placements'
                        or caller == 'number_combinations'):
                    return "", x_value, y_value

        else:  # If User input string
            x_value = "You should enter digit"
            y_value = "You should enter digit"

            # caller INDEX #
            if caller == 'index':
                return "", "", "", "", x_value, y_value

            # caller COMPLEMENT | PERMUTATIONS | PLACEMENTS | COMBINATIONS #
            if (caller == 'complement' or caller == 'number_permutations' or caller == 'number_placements'
                    or caller == 'number_combinations'):
                return "", x_value, y_value

    # IF USER'S NUMBERS IS TOO LARGE #
    except ValueError and OverflowError:
        x_value = "Your Number Is Too Large"
        y_value = "Your Number Is Too Large"

        # caller INDEX #
        if caller == 'index':
            return "", "", "", "", x_value, y_value

        # caller COMPLEMENT | PERMUTATIONS | PLACEMENTS | COMBINATIONS #
        if (caller == 'complement' or caller == 'number_permutations' or caller == 'number_placements'
                or caller == 'number_combinations'):
            return "", x_value, y_value
