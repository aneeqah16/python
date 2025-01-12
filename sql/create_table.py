import mysql.connector as sqc

mydb = sqc.connect(
    host="localhost",
    user="root",
    password="new_password"
)
print(mydb)
# printing connection
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS test2.test2_table(c1 INT, c2 VARCHAR(255), c3 FLOAT, c4 INT , c5 VARCHAR(255))")

# closing the database
mydb.close()
