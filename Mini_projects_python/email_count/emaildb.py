import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts(org TEXT, count INTEGER)''')

fhand = open("mbox.txt")
dic = dict()
for line in fhand:
    if line.startswith("From: "):
        email = line.split()[1]
        org = email[email.find('@')+1:]
        dic[org] = dic.get(org,0)+1

for item in dic:
    print(item,dic[item])
    cur.execute('''INSERT INTO Counts (org, count)VALUES (?, ?)''', (item,dic[item]))

conn.commit()
cur.close()
