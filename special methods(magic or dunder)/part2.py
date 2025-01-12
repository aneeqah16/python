# Define a class named 'institution1'
class institution1: 

    # __init__ is the constructor method, used for initializing object attributes
    def __init__(self):
        self.mobile_number = 6756757765  # Initialize the mobile_number attribute of the object

    # __str__ is a special method that is automatically called when you print an object
    def __str__(self):
        return "this is my magic call of str"  # Return a custom string representation of the object

# Create an instance (object) of the institution1 class
obj1 = institution1()

# Print the object. The __str__ method will be called automatically when you print the object
print(obj1)
