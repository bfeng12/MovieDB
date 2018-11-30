CREATE DATABASE MovieDB;

CREATE TABLE Person(
	ID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK(Age < 200 AND Age >= 0),
    PRIMARY KEY(ID)
);

CREATE TABLE Actor(
	ID int NOT NULL,
    FOREIGN KEY (ID) REFERENCES Person(ID)
		ON DELETE CASCADE,
    PRIMARY KEY(ID)
);
CREATE TABLE Producer(
	ID int NOT NULL,
    FOREIGN KEY (ID) REFERENCES Person(ID)
		ON DELETE CASCADE,
    PRIMARY KEY(ID)
);
CREATE TABLE Director(
	ID int NOT NULL,
    FOREIGN KEY (ID) REFERENCES Person(ID)
		ON DELETE CASCADE,
    PRIMARY KEY(ID)
);
CREATE TABLE Award(
	ID int NOT NULL AUTO_INCREMENT,
    awardName varchar(64),
    awardType char(10),
    CHECK (awardType IN ('Oscar','Golden Globe','Nobel','National Film Award')),
    PRIMARY KEY(ID)
);
CREATE TABLE Movie(
	ID int NOT NULL AUTO_INCREMENT,
    movieName CHAR(64),
    rating FLOAT(4,2) ,
    parentalRating varchar(64) DEFAULT 'NR', 
    releaseDate DATE,
    
    CONSTRAINT ckParentalRating CHECK (rating IN ('PG-13','PG','R','NR','G')),
    CHECK (rating >= 0 AND rating <= 10),
    PRIMARY KEY(ID)
);
CREATE TABLE Distributor(
	ID int NOT NULL AUTO_INCREMENT,
    yearFounded int,
    netWorth int,
    distributorName varchar(64) UNIQUE,
    headquarters varchar (64),
    
    CHECK(netWorth >= 0),
    CHECK(yearFounded <= YEAR(CURDATE()) AND yearFounded >= 1890),
    PRIMARY KEY (ID)
);

-- The other relationship tables
CREATE TABLE Owns(
	dateAwarded DATE,
    awardID int,
    personID int,
    
    FOREIGN KEY(awardID) REFERENCES Award(ID)
		ON DELETE CASCADE,
    FOREIGN KEY(personID) REFERENCES Person(ID)
		ON DELETE CASCADE,
    PRIMARY KEY(awardID, personID)
);

CREATE TABLE Distributes(
	region varchar(32),
    distributorID int,
    movieID int,
    
    FOREIGN KEY (movieID) REFERENCES Movie(ID)
		ON DELETE CASCADE,
    FOREIGN KEY (distributorID) REFERENCES Distributor(ID)
		ON DELETE CASCADE,
    PRIMARY KEY(distributorID, movieID)
);

CREATE TABLE Casts(
	directorID int NOT NULL,
    producerID int NOT NULL,
    movieID int NOT NULL,
    
    FOREIGN KEY (directorID) REFERENCES Director(ID),
    FOREIGN KEY (producerID) REFERENCES Producer(ID),
    FOREIGN KEY (movieID) REFERENCES Movie(ID)
		ON DELETE CASCADE,
    PRIMARY KEY(movieID)
);
CREATE TABLE CastsActor(
	movieID int NOT NULL,
    actorID int NOT NULL,
    FOREIGN KEY (movieID) REFERENCES Movie(ID)
		ON DELETE CASCADE,
    FOREIGN KEY (actorID) REFERENCES Actor(ID),
    PRIMARY KEY (movieID, actorID)
);
