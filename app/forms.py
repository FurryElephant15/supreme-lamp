from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, EmailField, FileField, DateTimeField, RadioField
from wtforms.validators import DataRequired
class SignUp(FlaskForm): #form that handles signups
    OrganizationName = StringField('Organization Name', validators=[DataRequired()])
    emails = EmailField("Organization Email")
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
class LogIn(FlaskForm): #form that handles logins
    emails = EmailField("Organization Email")
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
class postForm(FlaskForm): #handles posts
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    imageA = FileField('Upload Image')
    imageB = FileField('Upload Image')
    imageC = FileField('Upload Image')
    city = RadioField(choices=[("tampa", "Tampa"),("miami", "Miami"),("orlando", "Orlando")])
    time=DateTimeField()
    submit = SubmitField('Submit')

