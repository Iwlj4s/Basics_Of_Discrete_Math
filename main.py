from flask import Flask, render_template, request

from form import SetsForm, ComplementForm, FindNumberPermutationForm
from form import FindNumberPlacementsForm, FindNumberCombinationsForm

from main_functions.get_all_main_results import full_checked_results

from data import index_data, complement_data, find_number_permutation_data
from data import find_number_placements_data, find_number_combinations_data

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


# PERMUTATIONS PAGE #
@app.route('/number_permutations', methods=['GET', 'POST'])
def number_permutations():
    permutations_form = FindNumberPermutationForm()

    if request.method == 'POST' and permutations_form.validate_on_submit():
        (res_permutations, x_value, y_value) = full_checked_results(x=permutations_form.user_n_value.data, y="",
                                                                    x_value=permutations_form.user_n_value.data,
                                                                    y_value="")

        permutations_form.user_n_value.data = x_value

        return render_template('number_permutations.html', permutations_form=permutations_form,
                               find_number_permutation_data=find_number_permutation_data,
                               res_permutations=res_permutations)
    return render_template('number_permutations.html', permutations_form=permutations_form,
                           find_number_permutation_data=find_number_permutation_data)


# PLACEMENTS PAGE #
@app.route('/number_placements', methods=['GET', 'POST'])
def number_placements():
    placements_form = FindNumberPlacementsForm()

    if request.method == 'POST' and placements_form.validate_on_submit():
        (res_placements, x_value, y_value) = full_checked_results(x=placements_form.user_n_value.data,
                                                                  y=placements_form.user_k_value.data,
                                                                  x_value=placements_form.user_n_value.data,
                                                                  y_value=placements_form.user_k_value.data)

        placements_form.user_n_value.data = x_value
        placements_form.user_k_value.data = y_value

        return render_template('number_placements.html', placements_form=placements_form,
                               find_number_placements_data=find_number_placements_data,
                               res_placements=res_placements)

    return render_template('number_placements.html', placements_form=placements_form,
                           find_number_placements_data=find_number_placements_data)


# COMBINATIONS PAGE #
@app.route('/number_combinations', methods=['GET', 'POST'])
def number_combinations():
    combinations_form = FindNumberCombinationsForm()
    if request.method == 'POST' and combinations_form.validate_on_submit():
        (res_combinations, x_value, y_value) = full_checked_results(x=combinations_form.user_n_value.data,
                                                                    y=combinations_form.user_k_value.data,
                                                                    x_value=combinations_form.user_n_value.data,
                                                                    y_value=combinations_form.user_k_value.data)

        combinations_form.user_n_value.data = x_value
        combinations_form.user_k_value.data = y_value

        return render_template('number_combinations.html', combinations_form=combinations_form,
                               find_number_combinations_data=find_number_combinations_data,
                               res_combinations=res_combinations)
    return render_template('number_combinations.html', combinations_form=combinations_form,
                           find_number_combinations_data=find_number_combinations_data)


if __name__ == '__main__':
    app.run(debug=True)
