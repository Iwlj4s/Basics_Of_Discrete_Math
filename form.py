from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, SubmitField


class SetsForm(FlaskForm):
    user_a_value = FloatField('A = ')
    user_b_value = FloatField('B = ')

    user_submit_btn = SubmitField('Get Res')