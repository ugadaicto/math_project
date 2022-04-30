from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class QuizForm(FlaskForm):
    answer1 = SubmitField('A')
    answer2 = SubmitField('B')
    answer3 = SubmitField('C')
    answer4 = SubmitField('D')
    move_on = SubmitField('>')