from flask import Flask, jsonify, make_response, request, abort
import mysql.connector
#from flask_cors import CORS

app=Flask(__name__)
#CORS(app)

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="awesome",  # your password
                     db="movieDB")        # name of the data base
dbcursor = db.cursor()

@app.route('/')
def test():
    # Gets all the tables that are available in the MovieDB
    dbcursor.execute("SHOW TABLES")
    tables = dbcursor.fetchall()
    return jsonify({'tables':tables})
# ######################
# ##ALL THE MOVIE ONES##
# ######################
def movie_to_json(fetchall):
    # Turns an array returned from fetchallMethod() into a json file
    resultList = []
    for x in fetchall:
        tempDict = {
            'id': x[0],
            'movieName': x[1],
            'rating': x[2],
            'parentalRating': x[3],
            'releaseDate': x[4]
        }
        resultList.append(tempDict)
    return resultList


@app.route('/moviedb/movie/rating/<int:rating>', methods=['GET'])
def get_movies_rating(rating):
    # Gets movies where rating is greater than X
    query = "SELECT * FROM Movie WHERE rating >= (%s)"
    dbcursor.execute(query, [rating]);
    return jsonify(movie_to_json(dbcursor.fetchall()));


@app.route('/moviedb/movie/actor/<string:actor>', methods=['GET'])
def get_movies_actor(actor):
    # Gets the list of movies and actor has acted in
    query = \
    "SELECT DISTINCT firstName, Movie.ID, Movie.movieName, Movie.rating, Movie.parentalRating, Movie.releaseDate "\
    "FROM Movie, CastsActor, Actor, Person "\
    "WHERE Person.firstName = (%s) AND Movie.ID = CastsActor.movieID " \
    "AND Actor.ID = actorID"

    dbcursor.execute(query,[actor])
    resultList = []
    for x in dbcursor.fetchall():
        tempDict = {
            'actorName': x[0],
            'id': x[1],
            'movieName': x[2],
            'rating': x[3],
            'parentalRating': x[4],
            'releaseDate': x[5]
        }
        resultList.append(tempDict)
    return jsonify(resultList)


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
    return jsonify(resultList) 


@app.route('/moviedb/movie', methods=['GET'])
def get_movies():
    # Returns a json file of all movies in the MovieDB
    dbcursor.execute("SELECT * FROM Movie")
    return jsonify(movie_to_json(dbcursor.fetchall()))

@app.errorhandler(404)
def not_found(error):
    # If there is an error, return it as a Json file
    return make_response(jsonify({'error': 'Not found'}), 404)
#######################
##ALL THE PEOPLE ONES##
#######################
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


if __name__ == '__main__':
    app.run(debug=True)


