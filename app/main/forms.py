from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review Title', validators=[Required()])
    body = TextAreaField('Enter Your Review Here', validators=[Required()])
    reviewer = StringField('Reviewer', validators=[Required()])
    category = RadioField('Pick Category', choices=[('Shopping', 'Shopping'), ('Hotel', 'Hotel'), ('School', 'School'), ('Banks', 'Banks')], validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')

