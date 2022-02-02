from enum import unique, Enum
from app import db

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
    time = db.Column(db.DateTime(timezone=True))
    routetype = db.Column(db.Enum(RouteType))
    longitude = db.Column(db.Float, unique=False, nullable=False)
    latitude = db.Column(db.Float, unique=False, nullable=False)
    image = db.Column(db.String(120), nullable=False, default='default.jpg') 

    def __repr__(self):
        return '<Trail %r>' % self.name