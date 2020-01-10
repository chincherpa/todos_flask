from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
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
  comment_11 = StringField('comment_11')
  comment_12 = StringField('comment_12')
  comment_13 = StringField('comment_13')
  comment_14 = StringField('comment_14')
  comment_15 = StringField('comment_15')
  comment_16 = StringField('comment_16')
  comment_17 = StringField('comment_17')
  comment_18 = StringField('comment_18')
  comment_19 = StringField('comment_19')
  comment_20 = StringField('comment_20')
  new_comment = StringField('new_comment')
  tags = StringField('tags')
  reminder = DateField('reminder')
  submit = SubmitField('ok')
