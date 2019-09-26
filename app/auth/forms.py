
from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class SignupForm(FlaskForm):
    username=StringField("username", validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired(),Email()])
    location=StringField("location",validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("submit") 


    '''
    Custom Validation to ensure that a user with that username does not exist in our database.
    '''
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('A user with that username already exists.Please choose another user')
    
    '''
    Custom Validation to ensure that a user with that email does not exist in our database.
    '''

    def validate_email(swlf, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is already taken,please use another email.')

