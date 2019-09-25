from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    post = TextAreaField('Post Content', validators=[Required()])
    submit = SubmitField('Post')
