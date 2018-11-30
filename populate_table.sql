#SQL Script for Populating our table
#By Benny Feng
#Clear your database/tables before lightning bolting this

#CREATING PEOPLE
#1
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Coogler", "Ryan", 32);
INSERT INTO Director VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Producer VALUES ((SELECT LAST_INSERT_ID()));
#2
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Jordan", "Michael B.", 44);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#3
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Stallone", "Sylvester", 65);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Director VALUES ((SELECT LAST_INSERT_ID()));
#4
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Speilberg", "Steven", 68);
INSERT INTO Director VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Producer VALUES ((SELECT LAST_INSERT_ID()));
#5
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Gosling", "Ryan", 33);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#6
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Kunis", "Mila", 28);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#7
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Allen", "Tim", 59);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#8
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Pacino", "Al", 80);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Person (lastName, firstName, age) 
#9
VALUES ("Brando", "Marlon", 85);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#10
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Coppola", "Francis", 93);
INSERT INTO Director VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Producer VALUES ((SELECT LAST_INSERT_ID()));
#11
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Hemsworth", "Chris", 44);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#12
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Lee", "Stan", 97);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Producer VALUES((SELECT LAST_INSERT_ID()));
#13
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Miller", "Tim", 48);
INSERT INTO Director VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Producer VALUES((SELECT LAST_INSERT_ID()));
#14
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Downey Jr.", "Robert", 44);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#15
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Evans", "Chris", 32);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));
#16
INSERT INTO Person (lastName, firstName, age) 
VALUES ("Whedon", "Josh", 39);
INSERT INTO Director VALUES ((SELECT LAST_INSERT_ID()));
INSERT INTO Producer VALUES ((SELECT LAST_INSERT_ID()));

#Creed movie
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Creed", 8.2, "PG-13", "2015-11-25");
#Casts
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(1,1,1);
INSERT INTO CastsActor(movieID, actorID)
VALUES (1,2), (1,3);

#Creed2 Movie
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Creed 2", 7.35, "PG-13", "2018-12-10");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(1,1,2);
INSERT INTO CastsActor(movieID, actorID)
VALUES (2,2), (2,3);

#Godfather I
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Godfather I", 9.99, "R", "1973-06-10");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(10,10,3);
INSERT INTO CastsActor(movieID, actorID)
VALUES (3,8), (3,9);
#Godfather II
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Godfather II", 9.85, "R", "1976-06-10");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(10,10,4);
INSERT INTO CastsActor(movieID, actorID)
VALUES (4,8), (4,9);
#Godfather III
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Godfather III", 9.75, "R", "1979-06-10");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(10,10,5);
INSERT INTO CastsActor(movieID, actorID)
VALUES (5,8), (5,9);

#Deadpool
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Deadpool", 6.90, "R", "2016-07-15");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(13,13,6);
INSERT INTO CastsActor(movieID, actorID)
VALUES (6,5), (6,6),(6,12);
#Deadpool 2
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Deadpool II", 6.66, "R", "2018-08-11");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(13,13,7);
INSERT INTO CastsActor(movieID, actorID)
VALUES (7,5), (7,6), (7,12);
#Avengers
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("The Avengers", 8.16, "PG-13", "2012-07-05");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(16,16,8);
INSERT INTO CastsActor(movieID, actorID)
VALUES (8,14), (8,15), (8,12), (8,11);
#Avengers Infinity War
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Avengers: Infinity war", 8.92, "PG-13", "2018-06-05");
INSERT INTO Casts (directorID, producerID, movieID) 
VALUES(16,16,9);
INSERT INTO CastsActor(movieID, actorID)
VALUES (9,14), (9,15), (9,12), (9,11);

#AWARDS
#Sylvester Stallone
INSERT INTO Award (awardName, awardType)
VALUES ("Best Leading Actor", "Oscar");
INSERT INTO Owns(dateAwarded, awardID, personID)
VALUES ("2011-08-12", (SELECT LAST_INSERTED_ID()), 3);
#Stan Lee
INSERT INTO Award (awardName, awardType)
VALUES ("Best Supporting Actor", "Oscar");
INSERT INTO Owns(dateAwarded, awardID, personID)
VALUES ("2013-08-12", (SELECT LAST_INSERTED_ID()), 12);
#Al Pacino
INSERT INTO Award (awardName, awardType)
VALUES ("Best Actor of All Time", "Golden Globe");
INSERT INTO Owns(dateAwarded, awardID, personID)
VALUES ("1999-02-13", (SELECT LAST_INSERTED_ID()), 8);

INSERT INTO Award (awardName, awardType)
VALUES ("Best Leading Actor", "Oscar");
INSERT INTO Owns(dateAwarded, awardID, personID)
VALUES ("1977-05-19", (SELECT LAST_INSERTED_ID()), 8);



/*
INSERT INTO Person (lastName, firstName, age)
SELECT * FROM (SELECT 'Jordan', 'Michael', 44) AS tmMoviep
WHERE NOT EXISTS (
    SELECT firstName,lastName 
	FROM Person
	WHERE firstName = 'Michael' AND lastName = 'Jordan' AND age = 44
) LIMIT 1;
*/



