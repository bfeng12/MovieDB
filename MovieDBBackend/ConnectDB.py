#!/usr/bin/python
import mysql.connector

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="awesome",  # your password
                     db="MovieDB")        # name of the data base

print(db)
print("Hello world")
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM PERSON")

myresult = cur.fetchall()
resultList = []
for x in myresult:
    empDict = {
        'id': x[0],
        'firstName': x[1],
        'lastName': x[2],
        'age': x[3]
    }
    resultList.append(empDict)
print(resultList)
db.close()

def insert_person(age, firstname, lastname):
    query = "INSERT INTO PERSON VALUES (%s,%s,%s,%s)"
    args = (age,firstname,lastname)
    db.commit()


