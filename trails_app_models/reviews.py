import imp
from app import db
from enum import unique, Enum

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
