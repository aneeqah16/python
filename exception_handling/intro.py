# Example of handling file opening and writing with exception handling

# First, we attempt to open the file in write mode ("w")
try:
    # Opening the file "test.txt" in write mode
    f = open("test.txt", "w")
    
    # Writing some data into the file
    f.write("Write into my file")  # This writes "Write into my file" into the file
    f.close()  # Always close the file after performing the operation to avoid data loss or file locking

except Exception as e:
    # If there's an error (e.g., file not accessible), it will print the error message
    print("Error: ", e)

# Continue with other operations
print("hfgjhh")  # This is just an example print statement after the try-except block
