from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignupForm(FlaskForm):
    username=StringField("username", validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired(),Email()])
    location=StringField("location",validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("submit") 

