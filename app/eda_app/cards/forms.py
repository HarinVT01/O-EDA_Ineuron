from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

class CardForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')


class UploadForm(FlaskForm):
    fileName = FileField('Upload', validators=[FileAllowed(['wav'])])
    submit=SubmitField('Upload')