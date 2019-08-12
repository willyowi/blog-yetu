from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
#post form
class PostForm(FlaskForm):
    title = StringField('Post title',validators=[Required()])
    description = TextAreaField('About Post')
    submit = SubmitField('Submit')
#update

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

#reviews
class ReviewForm(FlaskForm):

 title = StringField('Review title',validators=[Required()])

 review = TextAreaField('Movie review')

 submit = SubmitField('Submit')

