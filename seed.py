from model import Users, Trails, Reviews
from model import connect_to_db, db
from csv import reader
from server import app


def load_trails():

    Trails.query.delete()


    print("Reading Trails seed file...")
    with open("seed_data/trails_seed.csv") as trail_seed:

        trails_reader = reader(trail_seed, delimiter=",")

        for row in trails_reader:
            trail = Trails(id=row[0],name=row[1],description=row[2],difficulty=row[3],length=row[4],elevation=row[5],routetype=row[6],latitude=row[7],longitude=row[8],time=row[10])
            db.session.add(trail)
            db.session.commit()    

    print("Successfully added trails data.")

def load_users():

    Users.query.delete()

    with open("seed_data/users_seed.csv") as user_seed:

        users_reader = reader(user_seed, delimiter=",")

        for row in users_reader:
            user = Users(id=row[0],name=row[1],email=row[2],password=row[3])
            db.session.add(user)
            db.session.commit()

def load_reviews():

    Reviews.query.delete()

    with open("seed_data/reviews_seed.csv") as review_seed:

        reviews_reader = reader(review_seed, delimiter=",")

        for row in reviews_reader:
            review = Reviews(id=row[0],user_id=row[1],trail_id=row[2],created=row[3],updated=row[4],comment=row[5],score=row[6])
            db.session.add(review)
            db.session.commit()

if __name__ == '__main__':
    import os

    # Upon running the file every time:
    # First, delete the test table(start with a new slate)
    # Second, create the test database anew
    os.system("dropdb test")
    os.system("createdb test")  

    connect_to_db(app)

    # create tables in case they haven't been created
    db.create_all()

    load_trails()
    load_users()
    #load_reviews()
