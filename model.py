"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    email = db.Column(db.String(64), 
                        nullable=True)
    password = db.Column(db.String(64), 
                        nullable=True)
    age = db.Column(db.Integer, 
                        nullable=True)
    zipcode = db.Column(db.String(15), 
                        nullable=True)

    def __repr__(self):
        """Show user info"""
        return f"User info: user_id={self.user_id} email={self.email}"


# Put your Movie and Rating model classes here.

class Rating(db.Model):
    """Raings of movies."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True)
    movie_id = db.Column(db.Integer)

    user_id = db.Column(db.Integer)

    score = db.Column(db.Integer)

    def __repr__(self):
        """Show rating info"""
        return f"Rating info: rating_id={self.rating_id} movie_id={self.movie_id} user_id={self.user_id}"


class Movie(db.Model):
    """Details of movies."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)
    title = db.Column(db.String(100))

    release_at = db.Column(db.DateTime)

    imdb_url = db.Column(db.String(200))

    def __repr__(self):
        """Show movie info"""
        return f"Movie info: movie_id={self.movie_id} title={self.title}"




##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
