# CHECK USER ENTER DATA #
def check_user_data(a, b):
    if len(a.replace(',', '')) and len(b.replace(',', '')) > 1:  # If user enter > 1
        return False
    else:  # If user enter < 1
        return True


# CHECK USER ENTER DIGIT #
def check_user_digit(a, b):
    a_digit = all(digit_a.isdigit() for digit_a in a)
    b_digit = all(digit_b.isdigit() for digit_b in b)

    if a_digit == True and b_digit == True:
        return True

    elif a_digit == False and b_digit == True:
        return False

    elif b_digit == False and a_digit == True:
        return False

    else:
        return False
