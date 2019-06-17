import json
import sqlite3

conn = sqlite3.connect('courses_students.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

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
''')

str = open("roster_data.json").read()
data = json.loads(str)

for item in data:
    name  = item[0]
    title = item[1]
    role = item[2]

    if name is None or title is None: continue
    
    cur.execute('INSERT OR IGNORE INTO User(name) VALUES(?)',(name,))
    cur.execute('SELECT id FROM User WHERE name = ?',(name,))
    user_id=cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES(?)',(title,))
    cur.execute('SELECT id FROM Course WHERE title = ?',(title,))
    course_id=cur.fetchone()[0]
    cur.execute('INSERT OR REPLACE INTO Member(course_id,user_id,role) VALUES(?,?,?)',(course_id,user_id,role))

conn.commit()
cur.close()
