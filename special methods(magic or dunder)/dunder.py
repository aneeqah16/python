# Print all the attributes and methods available for the int class.
# The dir() function returns a list of all attributes and methods for an object, 
# including dunder (double underscore) methods like __add__, __str__, etc.
print(dir(int))

# Example of using a dunder method (__add__) explicitly
# The + operator internally calls the __add__ method of the object
a = 100
print(a + 5)  # This calls the __add__ method internally (e.g., a.__add__(5))

# Instead of using the + operator, you can explicitly call the __add__ method on the object
# This is essentially the same as writing a + 5
print(a.__add__(5))  # Output: 105

# Dunder methods are special methods in Python that allow the interpreter to perform certain operations
# on objects, such as addition, subtraction, etc. These methods are automatically called 
# when you use the corresponding operator. For example:
# - __add__: called when you use the + operator
# - __sub__: called when you use the - operator
# - __mul__: called when you use the * operator
# And many more...

# Example of using the __new__ method, which is called before __init__ in object creation.

class Institution:
    # __new__ is a dunder method that gets called before __init__ when creating an object
    def __new__(cls):
        print("This is my new")
        # __new__ must return an instance of the class, usually by calling the parent class's __new__ method
        return super().__new__(cls)
       
    def __init__(self):
        print("This is my init")  # This is called after __new__
        self.mobile_number = 6756757765  # Assigning an attribute to the object

# Create an object of the Institution class
obj1 = Institution()

# The __new__ method is called first, printing "This is my new"
# The __init__ method is then called, printing "This is my init"
# We can access the mobile_number attribute of the object once the object is initialized
print(obj1.mobile_number)  # Output: 6756757765
