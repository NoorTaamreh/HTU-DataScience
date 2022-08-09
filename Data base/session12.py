import sqlite3

conn = sqlite3.connect('DataBase.db') #create new database

cur =conn.cursor() #we prefere to use it to deal with the query

# query = '''CREATE TABLE COMPANY(
#    ID INT PRIMARY KEY     NOT NULL,
#    NAME           TEXT    NOT NULL,
#    AGE            INT     NOT NULL,
#    ADDRESS        CHAR(50),
#    SALARY         REAL
# );''' 

# #when you write the query you must write in ''' Q '''

# cur.execute(query)


# query1 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 );"

# query2 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 );"

# query3 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );"


query4='''UPDATE COMPANY
SET NAME = 'Noor'
WHERE ID=1; '''
cur.execute(query4)

query5 ='''SELECT * from COMPANY'''

cur.execute(query5)
# cur.execute(query2)
# cur.execute(query3)

data = cur.execute(query5).fetchall()
print(data)


#conn.commit()
conn.close()

# import psycopg2
 # conn = psycopg2.connect(user="postgres", password="YOURPASSWORD", host="127.0.0.1", port="5432",database="postgres")
# cur= conn.cursor()
# query= "INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Rama', 32, 'Amman', 2000.00 );"
# cur.execute(query)
# conn.commit()
# conn.close()
