from flask import request
from flaskblog.models import User
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flaskblog.battleboats.actions import LessThan


class BattleBoatsSetUp(FlaskForm):
    rows = IntegerField('Enter row column size (3 to 12)', validators=[DataRequired(), NumberRange(min=3, max=12, message='Error, value must be more than 2 and less than 13')])
    columns = IntegerField('Enter board column size (3 to 12)', validators=[DataRequired(), NumberRange(min=3, max=12, message='Error, value must be more than 2 and less than 13')])
    rocks = IntegerField('Enter number of rocks', validators=[DataRequired()])
    submit = SubmitField('Start', id="begin_setup")

    def validate_rocks(self, rocks):
        rocks = rocks.data
        if rocks > (min(self.rows.data, self.columns.data)-2):
            raise ValidationError('Number of rocks must be from 0 to minimum(rows, columns)-2')

class PlaceRocks(FlaskForm):
    submit = SubmitField('Start', id="place_rocks")
