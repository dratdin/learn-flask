from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, TextAreaField
from wtforms.validators import URL, DataRequired, Length
from wtforms.widgets.html5 import DateInput


class TodoBaseForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    text = TextAreaField("Text", validators=[Length(max=3000)])
    url = StringField("URL", validators=[URL()])
    date = DateField("Date", widget=DateInput(), validators=[DataRequired()])


class TodoCreateForm(TodoBaseForm):
    submit = SubmitField("Create")


class TodoUpdateForm(TodoBaseForm):
    submit = SubmitField("Update")
