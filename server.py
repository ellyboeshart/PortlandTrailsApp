from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from trails_app_models.users import Users
from trails_app_models.trails import Trails
from trails_app_models.reviews import Reviews

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///trails_app"

db = SQLAlchemy(app)

@app.before_first_request
def before():
    db.create_all()

@app.route('/')
def get_base():
    return "<p>Hello, World!</p>"

@app.route('/users/<id>')
def get_user_by_id(id):
    user = Users.query.filter_by(id=id).first()

    return f"<p>Id: {user.id}, name: {user.name}, email: {user.email}, pass: {user.password}</p>"

@app.route('/trails/<id>')
def get_trail_by_id(id):
    trail = Trails.query.filter_by(id=id).first()

    return f"<p>Id: {trail.id}, name: {trail.name}, description = {trail.description}, difficulty: {trail.difficulty}, length: {trail.length}, elevation: {trail.elevation}, time: {trail.time}, route_type: {trail.routetype}, longitude: {trail.longitude}, latitude: {trail.latitude}</p>"

@app.route('/reviews/<id>')
def get_review_by_id(id):
    review = Reviews.query.filter_by(id=id).first()

    return f"<p>Id: {review.id}, user_id: {review.user_id}, trail_id: {review.trail_id}, created: {review.created}, updated: {review.updated}, comment: {review.comment}, score: {review.score}</p>"

if __name__ == '__main__':
   
    app.run(debug=True, host="0.0.0.0")
