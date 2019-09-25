from flask import render_template, redirect, url_for

from app.models import Blog, Comment
from app.main import main
from app.requests import getWeatherData

from .forms import BlogForm

from flask_login import login_required,current_user


@main.route('/')
def index():
    return render_template('index.html')

    weatherdata = getWeatherData()
    return render_template('index.html', weatherdata=weatherdata)


@main.route('/new-blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    form = BlogForm()
    if form.validate_on_submit():
        user_id = current_user._get_current_object().id
        new_blog = Blog(title=form.title.data, post=form.post.data, user_id=user_id)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html', form=form)

@main.route('/all_blogs')
def blogs():
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    return render_template('fammers_blog.html', blogs=blogs)

