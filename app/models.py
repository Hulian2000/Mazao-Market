from datetime import datetime

from flask_login import current_user, UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    image_path = db.Column(db.String(255), default='')
    datejoined = db.Column(db.DateTime, default=datetime.utcnow)
    hash_password = db.Column(db.String(255), nullable=False)
    post = db.relationship('Blog', backref='user', lazy='dynamic')
    like = db.relationship('Like', backref='user', lazy='dynamic')
    dislike = db.relationship('Dislike', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.hash_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "User: %s" % str(self.username)


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    post = db.Column(db.Text, nullable=False)
    dateposted = db.Column(db.DateTime, default=datetime.utcnow)
    like = db.relationship('Like', backref='blog', lazy='dynamic')
    dislike = db.relationship('Dislike', backref='blog', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship('Comment', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    def get_blog(id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    def __repr__(self):
        return f'Blog {self.post}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def get_comment(id):
        comment = Comment.query.all(id=id)
        return comment

    def __repr__(self):
        return f'Comment {self.comment}'


class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls, id):
        likes = Like.query.filter_by(blog_id=id).all()
        return likes

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'


class Dislike(db.Model):
    __tablename__ = 'dislikes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_dislikes(cls, id):
        dislikes = Dislike.query.filter_by(blog_id=id).all()
        return dislikes

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'
