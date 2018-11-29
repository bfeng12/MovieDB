#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort
import mysql.connector

app=Flask(__name__)
# Initializing the connection the to the database
db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="awesome",  # your password
                     db="MovieDB")        # name of the data base
dbcursor = db.cursor()
# TODO add PUT and DELETE Commands for the API


@app.route('/')
def tables():
    # Gets all the tables that are available in the MovieDB
    dbcursor.execute("SHOW TABLES")
    tables = dbcursor.fetchall()
    return jsonify({'tables': tables})


@app.route('/moviedb/movie/actor/<String:actor>', methods=['GET'])
def get_movies_actor(actor):
    # Gets the list of movies and actor has acted in
    query = "SELECT Movie.movieName " \
            "FROM Movie, CastsActor, Actor" \
            "WHERE Actor.firstName = (%s) AND Movie.ID = CastsActor.movieID AND Actor.ID = CastsActor.actorID"
    dbcursor.execute(query,actor)


@app.route('/moviedb/movie/year/<int:year>', methods=['GET'])
def get_movies_year(year):
    # Returns a json file of movies that were released in xxxx year
    dbcursor.execute("SELECT * FROM MOVIE WHERE Year(releaseDate) = (%s)", [year])
    resultList = []
    for x in dbcursor.fetchall():
        tempDict = {
            'id': x[0],
            'movieName': x[1],
            'rating': x[2],
            'parentalRating': x[3],
            'releaseDate': x[4]
        }
        resultList.append(tempDict)
    return jsonify({'movie': resultList})


@app.route('/moviedb/movie', methods=['GET'])
def get_movies():
    # Returns a json file of all movies in the MovieDB
    dbcursor.execute("SELECT * FROM MOVIE")
    resultList = []
    for x in dbcursor.fetchall():
        tempDict = {
            'id': x[0],
            'movieName': x[1],
            'rating': x[2],
            'parentalRating': x[3],
            'releaseDate': x[4]
        }
        resultList.append(tempDict)
    return jsonify({'movie': resultList})


@app.errorhandler(404)
def not_found(error):
    # If there is an error, return it as a Json file
    return make_response(jsonify({'error': 'Not found'}), 404)


""" 
Methods that alter people, not required for our project
"""
@app.route('/moviedb/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    # Returns a json file of a person given the ID
    dbcursor.execute("SELECT * FROM PERSON WHERE id = (%s)", [person_id])
    person = dbcursor.fetchall()
    return jsonify({'person':person})


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
    return jsonify({'person': dbcursor.fetchall()}), 201


@app.route('/moviedb/person', methods=['GET'])
def get_person():
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
    return jsonify({'people': resultList})


"""
def array_to_json(arrays):
    result = ""
    for x in arrays:
        temp = ""
        temp += "\"id\": " + x[0] + ",\n"
        temp += "\"firstName\": " + x[1] + ",\n"
        temp += "\"lastName:\" " + x[2] + ",\n"
        temp += "\"age\"" + x[3] + ",\n"
        result += temp
"""

if __name__ == '__main__':
    app.run(debug=True)


