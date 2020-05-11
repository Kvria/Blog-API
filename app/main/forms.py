from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
# from flask_login import login_required
from .. import db

class CommentForm(FlaskForm):

    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):

    title = StringField('TITLE',validators=[Required()])
    description = TextAreaField('BLOG POST.', validators=[Required()])
    submit = SubmitField('Submit')