from flask_sqlalchemy import SQLAlchemy 
from enum import unique, Enum

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can find
# the "session" object, where we do most of our interactions (committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class Difficulty(Enum):
    easy = "easy",
    moderate = "moderate",
    hard = "hard"

class RouteType(Enum):
    loop = "loop",
    out_and_back = "out and back"
    point_to_point = "point to point"

class Trails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False)
    description = db.Column(db.String(5000), unique=False, nullable=False)
    difficulty = db.Column(db.Enum(Difficulty))
    length = db.Column(db.Float(1), unique=False, nullable=False)
    elevation = db.Column(db.Integer, nullable = False)
    time = db.Column(db.Float)
    routetype = db.Column(db.Enum(RouteType))
    longitude = db.Column(db.Float, unique=False, nullable=False)
    latitude = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<Trail %r>' % self.name


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable = False)

    def __repr__(self):
        return f'<User id {self.id}, name {self.name}, email {self.email}, password {self.password}>'

class Score(Enum):
    one = "1",
    two = "2",
    three = "3",
    four = "4",
    five = "5"

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    trail_id = db.Column(db.Integer)
    created = db.Column(db.DateTime(timezone=True))
    updated = db.Column(db.DateTime(timezone=True))
    comment = db.Column(db.String(5000), unique=False, nullable=False)
    score = db.Column(db.Enum(Score))

    def __repr__(self):
        return '<Reviews %r>' % self.username


################################################################################
# Helper functions

def connect_to_db(app):
	"""Connect the database to our Flask app"""

	# Configure to use our PostgreSQL database
	app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///trails_app"
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	# As a convenience, if we run this module interactiverly, it will leave
	# you in a state of being able to work with the database directly.
	import os
	from server import app

	# Connect the Flask app to the database
	connect_to_db(app)

	# Will print when run interactively
	print("Connected to DB")

	# Make tables
	db.create_all()