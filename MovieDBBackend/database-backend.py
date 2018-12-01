#INSTRUCTIONS:
"""
To run this make sure you have downloaded flask. If you haven' do 'pip install flask'.
Also make sure you have mysql connector by doing 'pip install mysql.connector'.

Runs on "http://127.0.0.1:5000/"
"""
from flask import Flask, jsonify, make_response, request, abort
import mysql.connector
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
try:
    db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="awesome",  # your password
                     db="movieDB")        # name of the data base
except mysql.connector.errors.ProgrammingError:
    print("Error: Incorrect values for login.")
    exit(0)
dbcursor = db.cursor()

@app.route('/')
def home():
    # Gets all the tables that are available in the MovieDB
    dbcursor.execute("SHOW TABLES")
    tables = dbcursor.fetchall()
    return jsonify({'tables': tables})
# ######################
# ##ALL THE MOVIE ONES##
# ######################
def movie_to_json(fetchall):
    # Turns an array returned from fetchallMethod() into a json file
    resultList = []
    for x in fetchall:
        tempDict = {
            'id': x[0],
            'name': x[1],
            'rating': x[2],
            'parentalRating': x[3],
            'releaseDate': x[4]
        }
        resultList.append(tempDict)
    return resultList

@app.route('/moviedb/movie', methods=['POST'])
def insert_movie():
    # Insert a method using POST Method. Must be given a json file with constraints.
    reqData = request.get_json()
    query = "INSERT INTO MOVIE(movieName, rating, parentalRating, releaseDate) " \
            "VALUES (%s,%s,%s,%s)"
    movieName = reqData['movieName']
    rating = reqData['rating']
    parentalRating = reqData['parentalRating']
    releaseDate = reqData['releaseDate']
    vals = (movieName, rating, parentalRating, releaseDate)

    try:
        dbcursor.execute(query, vals)
        db.commit()
    except mysql.connector.errors.DatabaseError:
        return jsonify({'error': "incorrect values"})
    except KeyError:
        return jsonify({'error': "insufficient number of parameters"})

    return jsonify({'result': True})

@app.route('/moviedb/movie/update/<int:id>', methods=['PUT'])
def update_movie(id):
    query = "UPDATE Movie " \
            "SET movieName = (%s), rating = (%s), parentalRating = (%s), releaseDate = (%s) " \
            "WHERE ID = (%s)"
    reqData = request.get_json()
    movieName = reqData['movieName']
    rating = reqData['rating']
    parentalRating = reqData['parentalRating']
    releaseDate = reqData['releaseDate']
    vals = (movieName, rating,parentalRating, releaseDate, id)
    try:
        dbcursor.execute(query, vals)
        db.commit()
    except mysql.connector.errors.DatabaseError:
        return jsonify({'error': "incorrect values"})
    except KeyError:
        return jsonify({'error': "insufficient number of parameters"})
    return jsonify({'result': True})


@app.route('/moviedb/movie/parentalrating/delete/<string:rating>', methods=['DELETE'])
def delete_movies_parental_rating(rating):
    # Deletes the movie by parental rating
    rating = rating.upper()
    if rating != 'PG' and rating != 'PG-13' and rating != 'NR' and rating != 'R' and rating != 'G':
        return jsonify({'error': "incorrect rating"})
    query = "DELETE FROM MOVIE WHERE parentalRating = (%s)"
    dbcursor.execute(query, [rating])
    db.commit()
    return jsonify({'result': True})

@app.route('/moviedb/movie/parentalrating/<string:rating>', methods=['GET'])
def get_movies_parental_rating(rating):
    query = "SELECT * FROM Movie WHERE parentalRating = (%s)"
    dbcursor.execute(query,[rating])
    return jsonify(movie_to_json(dbcursor.fetchall()))


@app.route('/moviedb/movie/rating/<int:rating>', methods=['GET'])
def get_movies_rating(rating):
    # Gets movies where rating is greater than X
    query = "SELECT * FROM Movie WHERE rating >= (%s)"
    dbcursor.execute(query, [rating])
    return jsonify(movie_to_json(dbcursor.fetchall()))


@app.route('/moviedb/movie/actor/<string:actor>', methods=['GET'])
def get_movies_actor(actor):
    # Gets the list of movies an actor has acted in
    query = \
    "SELECT DISTINCT Movie.ID, Movie.movieName, Movie.rating, Movie.parentalRating, Movie.releaseDate "\
    "FROM Movie, CastsActor, Actor, Person "\
    "WHERE Person.firstName = (%s) AND Movie.ID = CastsActor.movieID " \
    "AND Actor.ID = CastsActor.actorID AND Person.ID = Actor.ID"

    dbcursor.execute(query,[actor])
    resultList = []
    for x in dbcursor.fetchall():
        tempDict = {
            'id': x[0],
            'name': x[1],
            'rating': x[2],
            'parentalRating': x[3],
            'releaseDate': x[4]
        }
        resultList.append(tempDict)
    return jsonify(resultList)


@app.route('/moviedb/movie/year/<int:year>', methods=['GET'])
def get_movies_year(year):
    # Returns a json file of movies that were released in xxxx year
    dbcursor.execute("SELECT * FROM MOVIE WHERE Year(releaseDate) = (%s)", [year])
    return jsonify(movie_to_json(dbcursor.fetchall()))

@app.route('/moviedb/movie', methods=['GET'])
def get_movies():
    # Returns a json file of all movies in the MovieDB
    dbcursor.execute("SELECT * FROM Movie")
    return jsonify(movie_to_json(dbcursor.fetchall()))

@app.route('/moviedb/movie/parentalrating/maximum', methods=['GET'])
def get_most_movies_by_parental_rating():
    # Returns a json file of all movies in the MovieDB
    dbcursor.execute("SELECT parentalRating, COUNT(*) From Movie GROUP BY parentalRating ORDER BY COUNT(*) DESC LIMIT 1")
    return jsonify(dbcursor.fetchone())

@app.errorhandler(404)
def not_found(error):
    # If there is an error, return it as a Json file
    return make_response(jsonify({'error': 'Not found'}), 404)
#######################
##ALL THE PEOPLE ONES##
#######################

"""
@app.route('/moviedb/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    # Returns a json file of a person given the ID
    dbcursor.execute("SELECT * FROM PERSON WHERE id = (%s)", [person_id])
    person = dbcursor.fetchall()
    return jsonify(person) 

@app.route('/moviedb/person', methods=['POST'])
def create_person():
    # Creates a person based off a POST request given a json file by the person doing the query.
    req_data = request.get_json()
    firstName = req_data['firstName']
    lastName = req_data['lastName']
    age = req_data['age']

    query = "INSERT INTO PERSON(lastName, firstName, Age) VALUES (%s,%s,%s)"
    values = (lastName, firstName, str(age))
    dbcursor.execute(query, values)
    db.commit()
    dbcursor.execute("SELECT * FROM PERSON")
    return jsonify(dbcursor.fetchall()), 201

@app.route('/moviedb/person', methods=['GET'])
def get_persons():
    # Gets all people (actor, director, etc.) from the MovieDB
    dbcursor.execute("SELECT * FROM PERSON")
    resultList = []
    for x in dbcursor.fetchall():
        empDict = {
            'id': x[0],
            'firstName': x[1],
            'lastName': x[2],
            'age': x[3]
        }
        resultList.append(empDict)
    return jsonify(resultList) 
"""

if __name__ == '__main__':
    app.run(debug=True)


