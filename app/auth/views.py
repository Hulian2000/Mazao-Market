from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.auth import auth
from .. import app, db
from app.models import User
from flask import render_template, url_for, flash, redirect
from .forms import SignupForm, LoginForm


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Wrong Username or Password')
    return render_template('auth/login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, location=form.location.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account has been created!", "success")
        return redirect(url_for('main.login'))
    return render_template('auth/signup.html', title="SignUp", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
