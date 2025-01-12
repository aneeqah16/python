# age = int(input("Enter your age"))
# print(age)
# We can enter any value in the input() function and it will be converted to a string automatically.
# However, since age cannot be negative, we can create custom exceptions to handle this.

class ValidateAge(Exception):
    # Inheriting from the Exception class to create a custom exception.
    
    def __init__(self, message):
        self.message = message
        # Calling the parent class's constructor to pass the message to it.
        # `super().__init__(self.message)` invokes the __init__ method of the parent class (Exception).
        super().__init__(self.message)  # This ensures that the error message is passed correctly to the base Exception class.


# Function to validate the age input
def validate_age(age):
    if age < 0:
        # If the age is less than 0, raise a custom exception with a specific message
        raise ValidateAge("Age cannot be negative")
    elif age > 200:
        # If the age is greater than 200, raise a custom exception with a different message
        raise ValidateAge("Age cannot be more than 200")
    else:
        # If the age is valid (between 0 and 200), return the age
        return age

# Try block where we ask for user input and validate the age
try:
    # Asking the user to enter their age
    age = int(input("Enter your age: "))  # Converting the input to an integer
    
    # Calling the validate_age function to check the validity of the entered age
    print(validate_age(age))

# Handle custom exception: If the age is invalid, it will raise ValidateAge
except ValidateAge as e:
    print(e)  # Print the custom error message from the ValidateAge exception

# Handle ValueError: This block will execute if the user does not enter a valid integer
except ValueError:
    print("Invalid input. Please enter a valid integer.")  # Inform the user about the invalid input
