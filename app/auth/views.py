from app.auth import auth
from .. import app,db,bcrypt
from app.models import User
from flask import render_template, url_for, flash, redirect
from .forms import SignupForm




@auth.route('/login')
def login():
    pass


@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, location=form.location.data, hash_password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account has been created!","success")
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html',title="SignUp", form=form )
    


@auth.route('/logout')
def logout():
    pass
