# Import the MySQL connector module with alias 'sqc'
import mysql.connector as sqc

# Establish a connection to the MySQL server
mydb = sqc.connect(
    host="localhost",  # The host where the MySQL server is running (usually localhost)
    user="root",       # The MySQL user with appropriate permissions (e.g., 'root')
    password="new_password"  # The password for the MySQL user
)

# Print the connection object to confirm connection
print(mydb)

# Create a cursor object to interact with the MySQL server
mycursor = mydb.cursor()

# Execute an SQL query to create a database named 'test2' if it doesn't exist already
mycursor.execute("CREATE DATABASE IF NOT EXISTS test2")

# Close the database connection after operations
mydb.close()
