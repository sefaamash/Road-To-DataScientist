import sqlite3

#connection
conn=sqlite3.connect('lunch.db')
c=conn.cursor()

#delete table
#c.execute('''DROP TABLE tablename''')

#create a table c.execute('''CREATE TABLE tabblename(colame TEXT, colname TEXT, colname INT)''')
c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')

#data to insertin each column
sandwich = 'chicken'
fruit = 'orange'
tablenum = 22

#insert and commit to database c.execute('''INSERT INTO tablename VALUES(?,?,?)''', (colname, fruit, tablenum))
c.execute('''INSERT INTO meals VALUES(?,?,?)''', (sandwich, fruit, tablenum))
conn.commit()

#select all data from table and print
c.execute('''SELECT * FROM meals''')
results=c.fetchall()
print(results)
c.execute('''DROP TABLE tablename''')