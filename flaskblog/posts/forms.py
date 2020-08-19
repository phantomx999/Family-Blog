from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=60)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
