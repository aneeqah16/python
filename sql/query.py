import mysql.connector as sqc

mydb = sqc.connect(
    host="localhost",
    user="root",
    password="new_password"
)
print(mydb)
# printing connection
mycursor = mydb.cursor()
# printing all columns: 
# mycursor.execute("select * from test2.test2_table")
# printing selective columns:
mycursor.execute("SELECT c1,c2 FROM test2.test2_table")
# executing query
for i in mycursor.fetchall():
    print(i)

# closing the database
mydb.close()
