from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from .forms import CommentForm, ReviewForm
from ..models import Review, Comment, User
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    Funvtion renderind index page and its content
    '''
    
    reviews = Review.query.all()

    return render_template('index.html', reviews = reviews)

@main.route('/shopping')
def shopping():
    
    shopping_review = Review.query.filter_by(category='shopping').all()
    
    return render_template('shopping.html', shopping = shopping_review)

@main.route('/hotel')
def hotel():
    
    hotel_review = Review.query.filter_by(category='hotel').all()
    
    return render_template('hotel.html', hotel = hotel_review)

@main.route('/school')
def school():
    
    school_review = Review.query.filter_by(category='school').all()
    
    return render_template('school.html', school = school_review)

@main.route('/bank')
def bank():
    
    bank_review = Review.query.filter_by(category='bank').all()
    
    return render_template('bank.html', bank = bank_review)


@main.route('/new', methods = ['GET', 'POST'])
@login_required
def new():

    review_form = ReviewForm()

    if review_form.validate_on_submit():
        title = review_form.title.data
        body = review_form.body.data
        reviewer = review_form.reviewer.data
        category = review_form.category.data

        new_review = Review(title = title, body = body, reviewer = reviewer, category = category, user_id= current_user.id)
        new_review.save_reviews()

        return redirect (url_for('main.index'))
    return render_template('new.html', review_form = review_form)

@main.route('/comment/<int:id>', methods = ['GET', 'POST'])
@login_required
def comment(id):
    
    comment_form = CommentForm()
    review = Review.query.get(id)

    if comment_form.validate_on_submit():
        title = comment_form.title.data
        comment = comment_form.comment.data

        new_comment = Comment(comment= comment, title = title, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.index'))
    return render_template('comment.html', comment_form = comment_form, review = review)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    '''
    Function that renders profile of user
    '''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('index.html', user=user)



