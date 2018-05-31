from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    '''
    defining subject
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    

    @property
    def password(self):
        raise AttributeError('Cannot read the password')


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Review {self.username}'


class Review(db.Model):
    '''
    Defining a review
    '''
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    reviewer = db.Column(db.String)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posted = db.Column(db.DateTime, default=datetime.utcnow)

    def save_reviews(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls):
        reviews = Review.query.all()
        return reviews

    @classmethod
    def get_categories(cls, category):
        review_cat = Review.query.filter_by(category=category)
        return review_cat

    all_reviews = []

    def __init__(self,title,body,reviewer,category,user_id):
        self.title = title
        self.body = body
        self.reviewer = reviewer
        self.category = category
        self.user_id = user_id


class Comment(db.Model):
    '''
    defining review object
    '''
    __tablename__= 'comments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls):
        comments = Comment.query.all()
        return comments

    all_comments = []

    def __init__(self,title,comment,user):
        self.title = title
        self.comment = comment
        self.user = user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))