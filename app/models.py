from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    role_id = db.Column(db.integer,db.ForeignKey('roles.id')
    posts = db.relationship('Post',backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),index = True)
    description = db.Column(db.String(255),unique = True,index = True)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'post', lazy = "dynamic")

class Comment(db.Model):
    __tablename__ = 'comments'

    all_comments = []

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255),index = True)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer , db.ForeignKey('posts.id'))

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,id,quote,author)
        self.id = id
        self.quote = quote
        self.author = author
