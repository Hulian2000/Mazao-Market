import os
import secrets
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth import auth
from .. import app, db, mail
from app.models import User
from flask import render_template, url_for, flash, redirect
from .forms import SignupForm, RequestResetForm, ResetPasswordForm
from flask_mail import Message





@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, location=form.location.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account has been created!","success")
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html',title="SignUp", form=form )



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))




###############################Reset Password using email#######################################################################################


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',sender='ndundirokamau@gmail.com',recipients=[user.email])                 
    msg.body = f'''To reset your password, visit the following link:
{url_for('auth.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@auth.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('app.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_request.html', title='Reset Password', form=form)




@auth.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('auth.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_token.html', title='Reset Password', form=form)


