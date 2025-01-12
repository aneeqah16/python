import logging

# Configure logging to capture errors with timestamps
logging.basicConfig(filename="errors_found.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Instruction 1: Always use a specific exception
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Avoid using generic exceptions
try:
    x = 5 / 0
except Exception as e:  # This is not recommended for specific errors
    print("An error occurred:", e)

# Instruction 2: Always print a proper error message
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please check your input.")

# Instruction 3: Always log the error
try:
    x = 5 / 0
except ZeroDivisionError as e:
    logging.error("Error: Division by zero is not allowed. Please check your input. Error details: %s", e)

# Instruction 4: Avoid writing multiple exception handlers unless necessary
# It’s better to handle exceptions more generically when there's no need for multiple blocks
# Example:
# try:
#     10 / 0
# except FileNotFoundError as e:
#     logging.error("Handling FileNotFoundError: %s", e)
# except ZeroDivisionError as e:
#     logging.error("Handling ZeroDivisionError: %s", e)
# except AttributeError as e:
#     logging.error("Handling AttributeError: %s", e)

# Instruction 5: Document all the errors for clarity
try:
    x = 5 / 0
except ZeroDivisionError as e:
    logging.error("Error: Division by zero is not allowed. Please check your input. Error details: %s", e)

# Instruction 6: Always use a generic exception when you're not expecting a specific error
try:
    x = 5 / 0
except Exception as e:
    logging.error("An unexpected error occurred. Error details: %s", e)

# Instruction 7: Cleanup all resources
try:
    with open("test.txt", "w") as f:
        f.write("This is my data written to the file.")
except FileNotFoundError as e:
    logging.error("Error: File not found: %s", e)
finally:
    # The `with` statement automatically handles closing the file, so no need to manually call f.close()
    print("Cleaning up resources.")
