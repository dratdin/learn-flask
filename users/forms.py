from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from .. import mongo


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=12)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8),],)
    confirm_password = PasswordField(
        "Confirm password", validators=[DataRequired(), EqualTo("password")]
    )

    submit = SubmitField("Sign Up")

    def validate_username(self, field):
        if mongo.db.users.find_one({"username": field.data}):
            raise ValidationError("That username is taken")

    def validate_email(self, field):
        if mongo.db.users.find_one({"email": field.data}):
            raise ValidationError("That email is taken")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()],)
    remember = BooleanField("Remember me")

    submit = SubmitField("Log In")
