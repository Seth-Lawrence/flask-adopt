"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm


from models import connect_db, Pet, db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def root():
    """list the pets by name, show photo, display availability"""

    pets = Pet.query.all()

    return render_template('index.html', pets=pets)


@app.route('/add', methods=["GET","POST"])
def add_pet():
    """Add pet form; handle adding a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(
            name=name, species=species, photo_url=photo_url,age=age)
            # Make this more legible add more apces and stuff
        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template('pet-form.html', form=form)


@app.route('/<int:pet_id>', methods=["GET","POST"])
def display_edit_form(pet_id):
    """displaying the add/edit form"""

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)



    if form.validate_on_submit():

        print("pet", pet)

        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        #  We just added a property. Be nervous that it didn't throw an error

        db.session.commit()

        return redirect("/")
    else:

        return render_template('display-edit.html',
                            pet=pet,
                            form=form)





# @app.route("/add", methods=["GET", "POST"])
# def add_snack():
#     """Snack add form; handle adding."""

#     form = AddSnackForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         price = form.price.data
#         # do stuff with data/insert to db

#         flash(f"Added {name} at {price}")
#         return redirect("/add")

#     else:
#         return render_template(
#             "snack_add_form.html", form=form)



