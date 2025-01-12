# Example of using a finally block in file operations

try:
    # Attempting to open the file in read mode
    f = open("test3.txt", "r")
    
    # Trying to write to the file, which will raise an error
    f.write("Hello, world!")  # This will raise an error because 'r' mode is read-only, and 'write' cannot be used in this mode.
    
    f.close()  # This line won't be executed if an error occurs before it

# The 'finally' block will execute no matter what, even if there is an exception in the try block
finally:
    print("File closed")  # This will always be printed regardless of whether an exception occurred or not
    # It's typically used for cleanup activities (like closing a file or releasing resources).
