from flask import Flask, render_template, request
from form import SetsForm, ComplementForm
from main_functions.get_all_main_results import full_checked_results
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
        (res_merge_a_b, res_intersection_a_b, res_difference_a_b,
         res_symm_diff_a_b, x_value, y_value) = full_checked_results(x=index_form.user_a_value.data,
                                                                     y=index_form.user_b_value.data,
                                                                     x_value=index_form.user_a_value.data,
                                                                     y_value=index_form.user_b_value.data)

        # IF user input digit or user input < 1 | X and Y values in INPUT Form
        index_form.user_a_value.data = x_value
        index_form.user_b_value.data = y_value

        # Return Result
        return render_template('index.html', index_form=index_form,
                               res_merge_a_b=res_merge_a_b,
                               res_intersection_a_b=res_intersection_a_b,
                               res_difference_a_b=res_difference_a_b,
                               res_symm_diff_a_b=res_symm_diff_a_b, index_data=index_data)

    return render_template('index.html', index_form=index_form, index_data=index_data)


# ----  COMPLEMENT PAGE ---- #
@app.route('/complement', methods=['GET', 'POST'])
def complement():
    complement_form = ComplementForm()

    if request.method == 'POST' and complement_form.validate_on_submit():
        # Init Check Functions #
        (res_complement, x_value, y_value) = full_checked_results(x=complement_form.user_U_value.data,
                                                                  y=complement_form.user_a_value.data,
                                                                  x_value=complement_form.user_U_value.data,
                                                                  y_value=complement_form.user_a_value.data)

        # IF user input digit or user input < 1  X and Y values in INPUT Form
        complement_form.user_a_value.data = y_value
        complement_form.user_U_value.data = x_value

        # Return Result
        return render_template('complement.html', complement_form=complement_form,
                               res_complement=res_complement, complement_data=complement_data)

    return render_template('complement.html', complement_form=complement_form,
                           complement_data=complement_data)


if __name__ == '__main__':
    app.run(debug=True)
