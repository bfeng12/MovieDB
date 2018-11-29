#SQL Script for Populating our table
#By Benny Feng

#Creed movie
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Creed", 8.2, "PG-13", 2015-11-25);

INSERT INTO Person (lastName, firstName, age) 
VALUES ("Coogler", "Ryan", 32);
INSERT INTO Director VALUES ((SELECT LAST_INSERT_ID()));

INSERT INTO Person (lastName, firstName, age) 
VALUES ("Jordan", "Michael", 44);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));

INSERT INTO Person (lastName, firstName, age) 
VALUES ("Stallone", "Sylvester", 65);
INSERT INTO Actor VALUES ((SELECT LAST_INSERT_ID()));

INSERT INTO Casts (directorId,producerId,movieId)
VALUES ((SELECT MAX(ID) FROM Director), (SELECT MAX(ID) FROM Producer), (SELECT MAX(ID) FROM Movie));

INSERT INTO CastsActor
VALUES ((SELECT ID FROM Person WHERE lastName = 'Stallone' AND firstName = 'Sylvester' LIMIT 1),
		(SELECT ID FROM Movie WHERE movieName = 'Creed' LIMIT 1));
        
INSERT INTO CastsActor
VALUES ((SELECT ID FROM Person WHERE lastName = 'Jordan' AND firstName = 'Michael' LIMIT 1),
		(SELECT ID FROM Movie WHERE movieName = 'Creed' LIMIT 1));


#Creed2 Movie
INSERT INTO Movie (movieName, rating, parentalRating, releaseDate) 
VALUES ("Creed 2", 7.35, "PG-13", 2018-12-10);

INSERT INTO Person (lastName, firstName, age)
SELECT * FROM (SELECT 'Jordan', 'Michael', 44) AS tmp
WHERE NOT EXISTS (
    SELECT firstName,lastName 
	FROM Person
	WHERE firstName = 'Michael' AND lastName = 'Jordan' AND age = 44
) LIMIT 1;

INSERT INTO Actor
SELECT * FROM (SELECT 


