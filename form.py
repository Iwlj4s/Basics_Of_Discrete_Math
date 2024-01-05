from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField


# Main form for user input
class SetsForm(FlaskForm):
    user_a_value = StringField('A = ')
    user_b_value = StringField('B = ')

    user_submit_btn = SubmitField('Get Res')


class ComplementForm(FlaskForm):
    user_a_value = StringField('X = ')
    user_U_value = StringField('U = ')

    user_submit_btn = SubmitField('Get Res')


class FindNumberPermutationForm(FlaskForm):
    user_n_value = StringField('n = ')

    user_submit_btn = SubmitField('Get Res')


class FindNumberPlacementsForm(FlaskForm):
    user_n_value = StringField('n = ')
    user_k_value = StringField('k = ')

    user_submit_btn = SubmitField('Get Res')


class FindNumberCombinationsForm(FlaskForm):
    user_n_value = StringField('n = ')
    user_k_value = StringField('k = ')

    user_submit_btn = SubmitField('Get Res')