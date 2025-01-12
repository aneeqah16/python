# Example of using try-else block for file operations

try:
    # Attempting to open the file in write mode
    f = open("test1.txt", "w")
    
    # Writing some text into the file
    f.write("Hello, Python!")  # Writes "Hello, Python!" to the file
    f.close()  # Always close the file after performing the operation
    
except Exception as e:
    # If there is an error (e.g., file cannot be opened, write permission error, etc.)
    print("An error occurred: ", str(e))

else:
    # If no exceptions are thrown in the try block, this block will run
    print("File has been created and written successfully")
    # This message will be printed only if the file was created and written to without errors
