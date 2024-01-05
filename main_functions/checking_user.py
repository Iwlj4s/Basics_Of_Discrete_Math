# CHECK USER ENTER DATA #
def check_user_data(a, b):
    if len(a.replace(',', '')) and len(b.replace(',', '')) > 0:  # If user enter > 1
        return False

    else:  # If user enter < 1
        return True


# CHECK USER ENTER DIGIT #
def check_user_digit(a, b):
    a_digit = all(digit_a.replace('-', '').isnumeric() for digit_a in a.split())
    b_digit = all(digit_b.replace('-', '').isnumeric() for digit_b in b.split())

    if a_digit == True and b_digit == True:
        return True

    elif a_digit == False and b_digit == True:
        return False

    elif b_digit == False and a_digit == True:
        return False

    else:
        return False


# IF ENTER IS ONE NUMBER #

# User Enter Data #
def check_user_data_for_one_number(x):
    if len(x.replace(',', '')) > 0:
        return False

    else:
        return True


# User Enter Digit#
def check_user_digit_for_one_number(x):
    a_digit = all(digit_a.replace('-', '').isnumeric() for digit_a in x.split())

    if a_digit:
        return True
    else:
        return False


# CHECK FOR N > K #
def check_user_n_k(n, k):
    if n > k or n == k:
        return True

    else:
        return False

