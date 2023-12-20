from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, SubmitField


class SetsForm(FlaskForm):
    user_a_value = StringField('A = ')
    user_b_value = StringField('B = ')

    user_submit_btn = SubmitField('Get Res')