This python script reads details of songs from an xml file and store the data in a database with following schema.

CREATE TABLE Artist(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Genre (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name    TEXT UNIQUE);
CREATE TABLE Album (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,artist_id  INTEGER,title  TEXT UNIQUE);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
