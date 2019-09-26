class LoginForm(FlaskForm):
    username=StringField("userbane", validators=[DataRequired()])
    email=StringField("email", validators=[DataRequired()])
    password=PasswordField("password", validators=[DataRequired()])
    rememberme=BooleanField("remember me")
    submit=SubmitField("Log in")
