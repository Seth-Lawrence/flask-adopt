"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SelectField
from wtforms.validators import InputRequired, URL

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])
    species = SelectField(
        "Species",
        choices=[('cat','Cat',),('dog','Dog'),('porc','Porcupine')],
        validators=[InputRequired()])
    photo_url = StringField(
        "Photo URL",
        validators=[URL(require_tld=True)])
    age = SelectField(
        "Age",
        choices=[(1,"baby"),(2,"young"),(3,"adult"),(4,"senior")])
    notes = TextAreaField("Notes")





