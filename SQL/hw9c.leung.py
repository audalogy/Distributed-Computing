import sqlite3

from ggplot import *
from pandas import DataFrame

conn = sqlite3.connect("track_metadata.db")
cur = conn.cursor()

data_2 = []

for row in cur.execute('''select count(*), year from songs\
	where songs.artist_name='Rick Astley'
	group by songs.year  '''):
	if not row[1]==0:
		data_2.append({'songs': row[0], 'year': row[1]})

print data_2

release_data = DataFrame(data_2)


print ggplot(aes(x='year', y='songs'), data=release_data) + \
    geom_point(color='blue') + \
    geom_line(alpha=0.30) + \
    stat_smooth(span=.075, color='black') + \
    ggtitle("Rick Astley Tracks Released By Year") + \
    xlab("Year") + \
    ylab("Songs")