from sqlalchemy import Column
from app import db

class Users(db.Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(120), unique=True, nullable=False)
    password = Column(db.String(30), unique=False, nullable = False)

    def __repr__(self):
        return f'<User id {self.id}, name {self.name}, email {self.email}, password {self.password}>'