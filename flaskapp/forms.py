from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    comment_1 = StringField('comment_1')
    comment_2 = StringField('comment_2')
    comment_3 = StringField('comment_3')
    comment_4 = StringField('comment_4')
    comment_5 = StringField('comment_5')
    comment_6 = StringField('comment_6')
    comment_7 = StringField('comment_7')
    comment_8 = StringField('comment_8')
    comment_9 = StringField('comment_9')
    comment_10 = StringField('comment_10')
    new_comment = StringField('new_comment')
    submit = SubmitField('ok')
