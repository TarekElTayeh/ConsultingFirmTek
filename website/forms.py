"""Form definitions for authentication views."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Email, InputRequired, Length


class CredentialsForm(FlaskForm):
    """Base form providing email and password fields."""

    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])


class LoginForm(CredentialsForm):
    """Form for logging in existing users."""

    submit = SubmitField("Log In")


class SignupForm(CredentialsForm):
    """Form for registering new users."""

    submit = SubmitField("Sign Up")
