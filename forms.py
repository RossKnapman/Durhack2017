from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class SearchForm(Form):
    lat_a = StringField('lat_a', validators=[DataRequired()])
    long_a = StringField('long_a')
    lat_b = StringField('lat_b')
    long_b = StringField('long_b')