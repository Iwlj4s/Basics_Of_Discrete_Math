from flask import Flask, render_template, request
from form import SetsForm
from main_functions.get_res import get_result

import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SetsForm()
    print('Before get result')

    if request.method == 'POST' and form.validate_on_submit():
        a = form.user_a_value.data.replace(',', '').split()
        b = form.user_b_value.data.replace(',', '').split()

        res_merge_a_b, res_intersection_a_b, res_difference_a_b, res_symm_diff_a_b = get_result(a, b)

        print(res_merge_a_b)
        print(res_intersection_a_b)
        print(res_difference_a_b)
        print(res_symm_diff_a_b)

        return render_template('index.html', form=form,
                               res_merge_a_b=res_merge_a_b,
                               res_intersection_a_b=res_intersection_a_b,
                               res_difference_a_b=res_difference_a_b,
                               res_symm_diff_a_b=res_symm_diff_a_b)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
