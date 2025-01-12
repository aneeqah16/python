import mysql.connector as sqc

mydb = sqc.connect(
    host="localhost",
    user="root",
    password="new_password"
)
print(mydb)
# printing connection
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)