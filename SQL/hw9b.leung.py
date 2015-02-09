import sqlite3

conn = sqlite3.connect('track_metadata.db')
cur = conn.cursor() 

q = "SELECT title FROM songs WHERE artist_name='The Beatles'"
res = conn.execute(q)
tracks = res.fetchall()
print tracks

