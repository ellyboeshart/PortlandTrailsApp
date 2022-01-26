from enum import unique, Enum
from trails_app_models.shared import db

class Difficulty(Enum):
    EASY = "easy",
    MODERATE = "moderate",
    HARD = "HARD"

class RouteType(Enum):
    LOOP = "loop",
    OUT_AND_BACK = "out and back",
    POINT_TO_POINT = "point to point"

class Trails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=False)
    description = db.Column(db.String(5000), unique=False, nullable=False)
    difficulty = db.Column(db.Enum(Difficulty))
    length = db.Column(db.Float(1), unique=False, nullable=False)
    elevation = db.Column(db.Integer, nullable = False)
    time = db.Column(db.DateTime(timezone=True))
    route_type = db.Column(db.Enum(RouteType))
    longitude = db.Column(db.Float, unique=False, nullable=False)
    latitude = db.Column(db.Float, unique=False, nullable=False)
    image = db.Column(db.String(120), nullable=False, default='default.jpg') 

    def __repr__(self):
        return '<Trail %r>' % self.name