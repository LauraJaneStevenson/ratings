"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session)

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template('homepage.html')


@app.route("/users")
def user_list():
    """ Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route("/register")
def register_user():
    """Shows registration page."""

    return render_template("register_form.html")


@app.route("/validate", methods=['POST'])
def validate_user():
    """Check to see if user exists or not, and add to database accordingly."""

    input_email = request.form.get("email")
    input_pw = request.form.get("password")
    input_age = request.form.get("age")
    input_zip = request.form.get("zipcode")


    if db.session.query(User).filter_by(email=input_email).first() == None:
        # instantiate new user
        new_user = User(email=input_email,
                        password=input_pw,
                        age=input_age,
                        zipcode=input_zip)

        # add the new user to the DB
        db.session.add(new_user)
        db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
