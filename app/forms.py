from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
 
class ContactForm(FlaskForm):
   name = StringField('name', validators=[DataRequired()])
   email = StringField('email', validators=[DataRequired(), Email()])
   message = TextAreaField('message', validators=[DataRequired()])
   send = SubmitField('send')
