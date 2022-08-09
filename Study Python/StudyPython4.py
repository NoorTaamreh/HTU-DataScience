import sqlite3
#create a new database if the database doesn't already exist
conn = sqlite3.connect('spider.sqlite')
#get a cursor object used to execute SQL commands
cur = conn.cursor()
#create the table
cur.execute('''CREATE TABLE IF NOT EXISTS Pages 
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,    
        error INTEGER, old_rank REAL, new_rank REAL)''')
#create the table

#create a new table if the table doesn't already exist

#connect to the database
conn = sqlite3.connect('spider.sqlite')
#create a cursor object
cur = conn.cursor()
#inert a new row of data
cur.execute('''INSERT OR IGNORE INTO Pages (url, html, error, old_rank)
    VALUES ( ?, NULL, 0, 0.0)''', (url,))   #(url, html, error, old_rank)   #(url, html, error, old_rank)       #(url, html, error, old_rank)
#commit the changes to the database     
conn.commit()
#close the database connection
#execute the sql statement
#commit the changes to the database
#close the database connection



