from flask import Flask, render_template, request
from form import SetsForm, ComplementForm
from main_functions.get_res import get_index_result, get_complement_result
from main_functions.checking_user import check_user_data, check_user_digit
from data import index_data, complement_data

import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY


# ----  Main "SETS" PAGE ---- #
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    index_form = SetsForm()

    if request.method == 'POST' and index_form.validate_on_submit():
        # Init Check Functions #

        # Check user enter is not nothing
        check_user_enter = check_user_data(a=index_form.user_a_value.data, b=index_form.user_b_value.data)

        # Replace , and spaces for check user entry digit
        check_user_enter_digit = check_user_digit(a=index_form.user_a_value.data.replace(',', '').replace(' ', ''),
                                                  b=index_form.user_b_value.data.replace(',', '').replace(' ', ''))
        # Checks #
        if check_user_enter_digit:
            if not check_user_enter:
                # If user Input digit
                a = index_form.user_a_value.data.replace(',', '').split()  # Get User Input Value
                b = index_form.user_b_value.data.replace(',', '').split()

                # Get Result
                res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b = get_index_result(a, b)

                return render_template('index.html', index_form=index_form,  # Return Res Data
                                       res_merge_a_b=res_merge_a_b,
                                       res_intersection_a_b=res_intersection_a_b,
                                       res_difference_a_b=res_difference_a_b,
                                       res_symm_diff_a_b=res_symm_diff_a_b, index_data=index_data)

            elif check_user_data:  # If User Input without anything
                index_form.user_a_value.data = "You should enter sets"
                index_form.user_b_value.data = "You should enter sets"

        else:  # If User input string
            index_form.user_a_value.data = "You should enter digit"
            index_form.user_b_value.data = "You should enter digit"

    return render_template('index.html', index_form=index_form, index_data=index_data)


# ----  COMPLEMENT PAGE ---- #
@app.route('/complement', methods=['GET', 'POST'])
def complement():
    complement_form = ComplementForm()

    if request.method == 'POST' and complement_form.validate_on_submit():
        # Init Check Functions #

        # Check user enter is not nothing
        check_user_enter = check_user_data(a=complement_form.user_a_value.data, b=complement_form.user_U_value.data)

        # Replace , and spaces for check user entry digit
        check_user_enter_digit = check_user_digit(a=complement_form.user_a_value.data.replace(',', '').replace(' ', ''),
                                                  b=complement_form.user_U_value.data.replace(',', '').replace(' ', ''))
        # Checks #
        if check_user_enter_digit:
            if not check_user_enter:
                # If user Input digit
                a = complement_form.user_a_value.data.replace(',', '').split()  # Get User Input Value
                u = complement_form.user_U_value.data.replace(',', '').split()

                # Get Result
                res_complement = get_complement_result(a=a, u=u)

                return render_template('complement.html', complement_form=complement_form,  # Return Res Data
                                       res_complement=res_complement,
                                       complement_data=complement_data)

            elif check_user_data:  # If User Input without anything
                complement_form.user_a_value.data = "You should enter sets"
                complement_form.user_U_value.data = "You should enter sets"

        else:  # If User input string
            complement_form.user_a_value.data = "You should enter digit"
            complement_form.user_U_value.data = "You should enter digit"

    return render_template('complement.html', complement_form=complement_form,
                           complement_data=complement_data)


if __name__ == '__main__':
    app.run(debug=True)
