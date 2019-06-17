import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Artist''')
cur.execute('''DROP TABLE IF EXISTS Genre''')
cur.execute('''DROP TABLE IF EXISTS Album''')
cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('''CREATE TABLE Artist(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE Genre (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name    TEXT UNIQUE)''')
cur.execute('''CREATE TABLE Album (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,artist_id  INTEGER,title  TEXT UNIQUE)''')
cur.execute('''CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)''')

def lookup(d, key):
    found = False
    for item in d:
        if found: return item.text
        if item.tag=='key' and item.text==key:
            found  =True
    return None

stuff = ET.parse('Library.xml')
lst = stuff.findall('dict/dict/dict')
for item in lst:
    if ( lookup(item, 'Track ID') is None ) : continue

    artist = lookup(item,'Artist')
    genre = lookup(item,'Genre')
    album = lookup(item,'Album')
    track = lookup(item,'Name')
    len = lookup(item,'Total Time')
    rating = lookup(item, 'Rating')
    count = lookup(item, 'Track Count')
    print(artist,genre,album,track,len,rating,count)
    if track is None or artist is None or album is None or genre is None:
        continue

    cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?)',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id=cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES (?)',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id=cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Album(title,artist_id) VALUES (?,?)',(album,artist_id,))
    cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
    album_id=cur.fetchone()[0]
    cur.execute('INSERT OR REPLACE INTO Track(title,album_id,genre_id,len,rating,count) VALUES(?,?,?,?,?,?)',(track,album_id,genre_id,len,rating,count,))

conn.commit()
cur.close()
