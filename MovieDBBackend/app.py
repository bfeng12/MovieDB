#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort
import mysql.connector

app=Flask(__name__)

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="awesome",  # your password
                     db="MovieDB")        # name of the data base
dbcursor = db.cursor()

@app.route('/')
def test():
    dbcursor.execute("SHOW TABLES")
    tables = dbcursor.fetchall()
    return jsonify({'tables':tables})
######################
##ALL THE MOVIE ONES##
######################
@app.route('/moviedb/movie/actor/<String:actor>', methods=['GET'])
def get_movies_actor(actor):
    query = "SELECT Movie.movieName " \
            "FROM Movie, CastsActor, Actor" \
            "WHERE Actor.firstName = (%s) AND Movie.ID = CastsActor.movieID AND Actor.ID = CastsActor.actorID"
    dbcursor.execute(query,actor)


@app.route('/moviedb/movie/year/<int:year>', methods=['GET'])
def get_movies_year(year):
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
    return make_response(jsonify({'error': 'Not found'}), 404)
#######################
##ALL THE PEOPLE ONES##
#######################
@app.route('/moviedb/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    dbcursor.execute("SELECT * FROM PERSON WHERE id = (%s)", [person_id])
    person = dbcursor.fetchall()
    return jsonify({'person':person})


@app.route('/moviedb/person', methods=['POST'])
def create_person():
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
def get_tasks():
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


def array_to_json(arrays):
    result = ""
    for x in arrays:
        temp = ""
        temp += "\"id\": " + x[0] + ",\n"
        temp += "\"firstName\": " + x[1] + ",\n"
        temp += "\"lastName:\" " + x[2] + ",\n"
        temp += "\"age\"" + x[3] + ",\n"
        result += temp

if __name__ == '__main__':
    app.run(debug=True)


