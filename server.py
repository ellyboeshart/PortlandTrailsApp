from unicodedata import name
from flask import Flask, jsonify, render_template, request, redirect, flash, session, send_file
from flask_sqlalchemy import SQLAlchemy
from model import Score, Users, Trails, Reviews
from model import connect_to_db
import googlemaps
import os 
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def get_base():
    return render_template("homepage.html", api_key=os.getenv('GOOGLE_MAPS_API_KEY'))

@app.route('/images/<file>')
def get_image(file):
    return send_file("images/" + file, mimetype='image/gif')

@app.route('/styles/<file>')
def get_css(file):
    return send_file("styles/" + file)


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
def get_review_by_trail_id(id):
    reviews = Reviews.query.filter_by(trail_id=id)

    reviews_list = []

    for cur_review in reviews:
        review = {
            'id':cur_review.id,
            'user_id':cur_review.user_id,
            'trail_id':cur_review.trail_id,
            'comment':cur_review.comment,
            'score':cur_review.score.value
        }
        reviews_list.append(review)

    return jsonify(reviews_list)

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
        session["user_id"] = user.id
        flash(f"Welcome back, {user.email}!")
        return redirect("/map")

@app.route('/logout')
def process_logout():
    "Process user logout"
    session.clear()
    return redirect("/")

@app.route('/review',methods = ['POST'])
def process_review():
    data = request.form
    print(data)
    trail_id = data['filter']
    id = Reviews.query.all()
    id = id[len(id) - 1].id + 1
    review = Reviews(id=id, trail_id=trail_id, user_id=1, comment=data['comment'], score=data['Score'])
    db.session.add(review)
    db.session.commit()
    flash("Review Added!")
    return redirect('/map')

@app.route("/map")
def get_gmap():
    """Get google map with trails information"""
    if session.get("user_email") == None:
        return redirect("/")

    all_trails = Trails.query.all()

    trailslist = []

    for trail in all_trails:
        marker = {
            "id": trail.id,
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
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.run(port=5000, host="0.0.0.0")
