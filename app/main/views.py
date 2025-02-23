from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required

from app.main import main
from app.models import Blog, Comment, Like, Dislike
from app.requests import getWeatherData, getAgriNews
from .forms import BlogForm, UpdateProfile
from .. import db

weatherdata = getWeatherData()
agrinews = getAgriNews()


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/weather')
def weather():
    return render_template('weather_data.html', weatherdata=weatherdata)


@main.route('/news')
def news():
    articles = getAgriNews()
    return render_template('news.html', articles=articles, current_user=current_user)


@main.route('/market')
def market():
    return render_template('market.html')


@main.route('/new-blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    form = BlogForm()
    if form.validate_on_submit():
        user_id = current_user._get_current_object().id
        new_blog = Blog(title=form.title.data, post=form.post.data, user_id=user_id)
        new_blog.save_blog()
        return redirect(url_for('main.blogs'))
    return render_template('new_blog.html', form=form)


@main.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.bio = form.bio.data
        current_user.location = form.location.data
        db.session.commit()
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.bio.data = current_user.bio
        form.location.data = current_user.location
    image_path = url_for('static', filename='images/' + current_user.image_path)
    return render_template('profile.html', image_path=image_path, form=form)


@main.route('/all_blogs')
def blogs():
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    return render_template('fammers_blog.html', blogs=blogs)


@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    comments = comments[::-1]
    blog = Blog.query.get(id)
    return render_template('blog.html', blog=blog, comments=comments)


@main.route('/comment/<blog_id>', methods=['GET', 'POST'])
@login_required
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment = request.form.get('newcomment')
    user_id = current_user._get_current_object().id
    new_comment = Comment(comment=comment, user_id=user_id, blog_id=blog_id)
    new_comment.save()
    return redirect(url_for('main.blogs', id=blog.id))


@main.route('/blog/<blog_id>/delete', methods=['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete_blog()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))


@main.route('/blog/<blog_id>/update', methods=['GET', 'POST'])
@login_required
def updateblog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.post = form.post.data
        db.session.commit()
        flash("You have updated your Blog!")
        return redirect(url_for('main.blogs', id=blog.id))
    if request.method == 'GET':
        form.title.data = blog.title
        form.post.data = blog.post
    return render_template('new_blog.html', form=form)


@main.route('/blog/like/<int:id>', methods=['POST', 'GET'])
@login_required
def like(id):
    get_likes = Like.get_likes(id)
    valid_string = f'{current_user.id}:{id}'
    for like in get_likes:
        to_str = f'{like}'
        if valid_string == to_str:
            return redirect(url_for('main.blogs', id=id))
        else:
            continue
    new_vote = Like(user=current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.blogs', id=id))


@main.route('/blog/dislike/<int:id>', methods=['POST', 'GET'])
@login_required
def dislike(id):
    get_dislikes = Dislike.get_dislikes(id)
    valid_string = f'{current_user.id}:{id}'
    for dislike in get_dislikes:
        to_str = f'{dislike}'
        if valid_string == to_str:
            return redirect(url_for('main.blogs', id=id))
        else:
            continue
    new_vote = Dislike(user=current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.blogs', id=id))
