from unicodedata import name
from flask import Flask, jsonify, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from trails_app_models.users import Users
from trails_app_models.trails import Trails
from trails_app_models.reviews import Reviews
import googlemaps
import os 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "dev"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///trails_app"

db = SQLAlchemy(app)

@app.before_first_request
def before():
    db.create_all()

@app.route('/')
def get_base():
    return render_template("homepage.html", api_key=os.getenv('GOOGLE_MAPS_API_KEY'))

@app.route('/users/<id>')
def get_user_by_id(id):
    user = Users.query.filter_by(id=id).first()

    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'pass': user.password
    })

@app.route('/trails/<id>')
def get_trail_by_id(id):
    trail = Trails.query.filter_by(id=id).first()

    return jsonify({
        'id': trail.id,
        'name': trail.name,
        'description': trail.description,
        'difficulty': trail.difficulty.value,
        'length': trail.length,
        'elevation': trail.elevation,
        'time': trail.time,
        'routetype': trail.routetype.value,
        'longitude': trail.longitude,
        'latitude': trail.latitude
    })

@app.route('/reviews/<id>')
def get_review_by_id(id):
    review = Reviews.query.filter_by(id=id).first()

    return jsonify({
        'id': review.id, 
        'user_id': review.user_id, 
        'trail_id': review.trail_id,
        'created': review.created, 
        'updated': review.updated,
        'comment': review.comment,
        'score': review.score.value
    })

@app.route('/sign_up',methods = ['POST'])
def process_sign_up():
    data = request.form
    id = Users.query.all()
    id = id[len(id) - 1].id + 1
    user = Users(id=id, name=data['username'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    flash("User Added!")
    return redirect('/')


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""
    data = request.form
    email = data["email"]
    password = data["password"]

    user = Users.query.filter_by(email=email).first()
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect("/")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")
        return redirect("/map")

@app.route('/review',methods = ['POST'])
def process_review():
    data = request.json
    review = Reviews(id=data['id'], user_id=data['user_id'], trail_id=data['trail_id'], comment=data['comment'], score=data['score'])
    db.session.add(review)
    db.session.commit()
    return get_review_by_id(data['id'])

@app.route("/map")
def get_gmap():
    """Get google map with trails information"""

    all_trails = Trails.query.all()

    trailslist = []

    for trail in all_trails:
        marker = {
            "name": trail.name,
            "long": trail.longitude,
            "lat": trail.latitude,
            "des": trail.description,
            "dif": trail.difficulty.value[0],
            "len": trail.length,
            "elv": trail.elevation,
            "tim": trail.time,
            "routetype": trail.routetype.value[0]
        }

        trailslist.append(marker)

      
    return render_template("map.html", api_key=os.getenv('GOOGLE_MAPS_API_KEY'), trailslist=trailslist)

if __name__ == '__main__':
   
    app.run(debug=True, host="0.0.0.0")
