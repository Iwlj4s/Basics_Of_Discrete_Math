from flask import Flask, render_template, request
from form import SetsForm
from main_functions.get_res import get_result
from main_functions.checking_user import check_user_data, check_user_digit
from data import index_data

import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY


# ----  HOME PAGE ---- #
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    form = SetsForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Init Check Functions #

        # Check user enter is not nothing
        check_user_enter = check_user_data(a=form.user_a_value.data, b=form.user_b_value.data)

        # Replace , and spaces for check user entry digit
        check_user_enter_digit = check_user_digit(a=form.user_a_value.data.replace(',', '').replace(' ', ''),
                                                  b=form.user_b_value.data.replace(',', '').replace(' ', ''))
        # Checks #
        if check_user_enter_digit:
            if not check_user_enter:
                # If user Input digit
                a = form.user_a_value.data.replace(',', '').split()  # Get User Input Value
                b = form.user_b_value.data.replace(',', '').split()

                res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b = get_result(a, b)  # Get Res

                return render_template('index.html', form=form,  # Return Res Data
                                       res_merge_a_b=res_merge_a_b,
                                       res_intersection_a_b=res_intersection_a_b,
                                       res_difference_a_b=res_difference_a_b,
                                       res_symm_diff_a_b=res_symm_diff_a_b, index_data=index_data)

            elif check_user_data:  # If User Input without anything
                form.user_a_value.data = "You should enter sets"
                form.user_b_value.data = "You should enter sets"

        else:  # If User input string
            form.user_a_value.data = "You should enter digit"
            form.user_b_value.data = "You should enter digit"

    return render_template('index.html', form=form, index_data=index_data)


# ----  COMPLEMENT PAGE ---- #
@app.route('/complement', methods=['GET', 'POST'])
def complement():
    return render_template('complement.html')


if __name__ == '__main__':
    app.run(debug=True)
