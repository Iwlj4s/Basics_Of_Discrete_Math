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
@app.route('/Home', methods=['GET', 'POST'])
def index():
    form = SetsForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
