
import sqlite3
import re 
# connect operation makes a “connection” to the database stored in the file 
# in the current directory. If the file does not exist, it will be created.
conn = sqlite3.connect('contacts.db') 
# A cursor is like a file handle that we can use to perform operations on the data stored in the database.
# Calling cursor() is very similar conceptually to calling open() when dealing with text files.
cur = conn.cursor()


#create a small SQLite database that contains the names, phone numbers, and address of four made-up people.  

cur.execute('DROP TABLE IF EXISTS Contact ')
cur.execute('CREATE TABLE Contact (name TEXT, phone INTEGER, address TEXT)')
cur.execute('INSERT INTO Contact (name, phone, address) VALUES ( ?, ?, ?)', ( 'Tiffany', 4088650225, '50 Merritt Way' ))
cur.execute('INSERT INTO Contact (name, phone, address) VALUES ( ?, ?, ?)', ('Linus',6509069885,'2468 California St'))
cur.execute('INSERT INTO Contact (name, phone, address) VALUES ( ?, ?, ?)', ('Rachel',4082561324,'201 Folsom St'))
cur.execute('INSERT INTO Contact (name, phone, address) VALUES ( ?, ?, ?)', ('Jonathan',7142805888,'One Marina Way'))
conn.commit()

# Add some more Python code to execute an SQL query on your database that grabs the address of 
# everyone whose name begins with a letter between M and Z inclusive. 

print 'Contact:'
cur.execute('SELECT name, address FROM Contact') 
for row in cur:
	for name in row[0]:
		if re.match("[M-Z]",name):
			print row[1]
conn.commit()

cur.close()

