from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Email
from flask_login import current_user
from ..models import User


class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    post = TextAreaField('Post Content', validators=[Required()])
    submit = SubmitField('Post')


class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required()])
    location = StringField('New location', validators=[Required()])
    bio = TextAreaField('Write a brief bio about you.', validators=[Required()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError("The username has already been taken")
