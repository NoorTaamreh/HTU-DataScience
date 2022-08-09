import sqlite3

conn = sqlite3.connect('DataBase2.db') 

cur =conn.cursor() 

# query = '''CREATE TABLE COMPANY(
#    ID INT PRIMARY KEY     NOT NULL,
#    NAME           TEXT    NOT NULL,
#    AGE            INT     NOT NULL,
#    ADDRESS        CHAR(50),
#    SALARY         REAL
# );''' 

# cur.execute(query)

query1 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 );"
query2 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'test', 32, 'California', 20000.00 );"

cur.execute(query1)
cur.execute(query2)


query5='''UPDATE COMPANY
SET NAME = 'Noor'
WHERE ID=1; '''
cur.execute(query5)

query4 ='''SELECT * from COMPANY'''
cur.execute(query4)

data = cur.execute(query4).fetchall()
print(data[0])
print(data)

#conn.commit()
conn.close()

