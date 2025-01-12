import mysql.connector as sqc

mydb = sqc.connect(
    host="localhost",
    user="root",
    password="new_password"
)
print(mydb)
# printing connection
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mycursor.execute("insert into test2.test2_table values(32,'anee' , 1000.00,675,'ashraf')")
mydb.commit()
# closing the database
mydb.close()
