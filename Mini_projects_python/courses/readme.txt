This python script creates a many to many database in sqlite3 with tables Course, User and a connector table Member with following schema.

CREATE TABLE User(
    name TEXT UNIQUE,
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE
);
CREATE TABLE Course(
    title TEXT UNIQUE,
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE
);
CREATE TABLE Member(
    course_id INTEGER,
    user_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id,course_id)
);

Data is collected from given json file (here 'roster_data.json') which contains user_name, course_title and role of user.
