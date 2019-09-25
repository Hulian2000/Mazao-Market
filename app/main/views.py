from flask import render_template, redirect, url_for

from app.models import Blog
from app.main import main

from .forms import BlogForm

from flask_login import login_required, current_user


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/blog')

def create_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(title=form.title.data, post=form.post.data, user_id=current_user.get_current_object().id)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', form=form)


