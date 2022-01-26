from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from trails_app_models import users, trails, reviews
from trails_app_models.shared import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
db.init_app(app)

with app.app_context():
  db.create_all()


@app.route('/')
def get():

    return "<p>Hello, World!</p>"

@app.route('/adduser/<user>')
def add_user(user):

    return f"<p>The user is {user}</p>"
    
# @app.route('/')
# def get():

#     return "<p>Hello, World!</p>"

if __name__ == '__main__':
   
    app.run(debug=True, host="0.0.0.0")
