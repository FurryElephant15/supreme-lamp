from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired
class SignUp(FlaskForm):
    OrganizationName = StringField('Organization Name', validators=[DataRequired()])
    emails = EmailField("Organization Email")
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('submit')
class LogIn(FlaskForm):
    emails = EmailField("Organization Email")
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('submit')
