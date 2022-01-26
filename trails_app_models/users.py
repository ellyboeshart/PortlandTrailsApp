from trails_app_models.shared import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable = False)

    def __repr__(self):
        return '<User id %r, name %r, email %r, password %r>' % self.id, self.name, self.email, self.password