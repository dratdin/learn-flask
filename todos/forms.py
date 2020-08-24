from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, URL


class TodoForm(Form):
    title = StringField('Title', validators=[DataRequired(), Length(max=255)])
    text = TextAreaField('Text', validators=[Length(max=3000)])
    url = StringField('URL', validators=[URL()])
    date = DateField('Date', validators=[DataRequired()])
