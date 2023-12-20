# CHECK USER ENTER DATA #
def check_user_data(a, b):
    if len(a.replace(',', '')) and len(b.replace(',', '')) > 1:  # If user enter > 1
        return False
    else:  # If user enter < 1
        return True


# CHECK USER ENTER DIGIT #
def check_user_digit(a, b):
    a_digit = False
    b_digit = False

    for digit_a in a:
        if digit_a.isdigit():
            return a_digit == True
        else:
            return a_digit == False

    for digit_b in b:
        if digit_b.isdigit():
            return b_digit == True
        else:
            return False

    if a_digit and b_digit == True:
        return True

    else:
        return False
