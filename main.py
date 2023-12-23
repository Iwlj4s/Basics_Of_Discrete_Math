from flask import Flask, render_template, request
from form import SetsForm
from main_functions.get_res import get_result
from main_functions.checking_user import check_user_data, check_user_digit

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

    check_user_enter = check_user_data(a=str(form.user_a_value.data), b=str(form.user_b_value.data))
    check_user_enter_digit = check_user_digit(a=str(form.user_a_value.data), b=str(form.user_b_value.data))

    if request.method == 'POST' and form.validate_on_submit():
        a = form.user_a_value.data.replace(',', '').split()     # Get User Input Value
        b = form.user_b_value.data.replace(',', '').split()

        if not check_user_enter_digit:
            if not check_user_enter:
                # If user Input digit
                res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b = get_result(a, b)

                return render_template('index.html', form=form,
                                       res_merge_a_b=res_merge_a_b,
                                       res_intersection_a_b=res_intersection_a_b,
                                       res_difference_a_b=res_difference_a_b,
                                       res_symm_diff_a_b=res_symm_diff_a_b)

            elif check_user_data:   # If User Input without anything
                form.user_a_value.data = "You should enter sets"
                form.user_b_value.data = "You should enter sets"

        else:   # If User input string
            form.user_a_value.data = "You should enter digit"
            form.user_b_value.data = "You should enter digit"

    return render_template('index.html', form=form)


# ----  COMPLEMENT PAGE ---- #
@app.route('/complement', methods=['GET', 'POST'])
def complement():
    return render_template('complement.html')


if __name__ == '__main__':
    app.run(debug=True)
