class CourseManager:

    def __init__(self, name, email):
        self.name = name  # Instance variable, specific to each object
        self.email = email  # Instance variable, specific to each object

    def student_details(self):
        print(self.name, self.email)  # Accessing instance variables


# Create an object of CourseManager and display name and email
course_manager = CourseManager("aneeqah", "aneeqah@gmail.com")   
print(course_manager.name)  # Access instance variable 'name'
print(course_manager.email)  # Access instance variable 'email'


class CourseManager1:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    # A class method that takes 'cls' as the first parameter
    # 'cls' refers to the class itself, not an instance.
    # Instead of using the __init__ method directly, we can use 'cls' to create an instance
    @classmethod
    def details(cls, name, email):
        return cls(name, email)  # Using 'cls' to instantiate the class, not the instance method

    def student_details(self):
        print(self.name, self.email)


# Using the class method to create an instance
course_manager1 = CourseManager1.details("eman", "eman@gmail.com")
# The 'details' class method uses 'cls' to instantiate the class, and it passes data (name, email) to it
print(course_manager1.name)
print(course_manager1.email)
course_manager1.student_details()


class CourseManager2:
    mobile_number = 8685687667  # Class variable, shared across all instances of the class
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # A class method that modifies the class variable
    @classmethod
    def change_number(cls, mobile):
        # Using 'cls' to modify the class variable 'mobile_number' for all instances
        CourseManager2.mobile_number = mobile  # Using class name directly or using cls (equivalent)

    def student_details(self):
        print(self.name, self.email)


# Create an object of CourseManager2 and display details
print("--------------------")
obj = CourseManager2("aneeqah", "aneeqah@gmail.com")
print(obj.mobile_number)  # Access class variable using the object
obj.change_number(787688567856)  # Change the class variable using the class method
print(obj.mobile_number)  # Access the updated class variable


class CourseManager3:
    mobile_number = 78688686788  # Class variable
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # A class method to modify class-level mobile number
    @classmethod
    def change_number(cls, mobile):
        CourseManager2.mobile_number = mobile  # Modifying the class-level mobile number using 'cls'
    
    # Another class method acting as an alternative constructor
    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, CourseManager3.mobile_number)


# Create instance using class method and display student details
course_manager3 = CourseManager3.details("anee", "anee@gmail.com")
course_manager3.student_details()


# External function added to the class
def course_details(cls, course_name):
    print("Course name is:", course_name)

# Adding external function to the class using classmethod
CourseManager3.course_details = classmethod(course_details)  # Adding 'course_details' as a class method
CourseManager3.course_details("Data Science Masters")  # Calling the external function


# Another external function added to the class to print mentor names
def mentor(cls, list_of_mentor):
    print(list_of_mentor)

# Adding mentor function to the class
CourseManager3.mentor = classmethod(mentor)  # Adding 'mentor' as a class method
CourseManager3.mentor(["aneeqah", "ashraf", "haamizah", "junaid"])  # Display list of mentors


# Demonstrating function deletion from class
class CourseManager4:
    mobile_number = 78688686788  # Class variable
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def change_number(cls, mobile):
        CourseManager4.mobile_number = mobile  # Modify class-level mobile number
    
    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, CourseManager3.mobile_number)


# Deleting a function using 'del' statement (removes method from the class)
del CourseManager4.change_number  # Removes 'change_number' method from the class
# Now if we try to call this method, it will throw an AttributeError

# Another way to delete a function in the class using 'delattr'
delattr(CourseManager4, "details")  # Deletes 'details' method from the class


# Can also delete other methods, including instance methods
delattr(CourseManager4, "student_details")  # Deletes 'student_details' method
# Now if we try to call the 'student_details' method, it will raise an AttributeError


# EXPLANATION OF 'cls' AND ITS USAGE:

# 'cls' stands for "class" and is used in class methods. 
# Unlike instance methods that use 'self' to refer to the current object instance, class methods use 'cls' 
# to refer to the class itself. This allows access to class-level variables and methods.

# Why do we use 'cls' instead of direct class names?
# - Using 'cls' makes the code more flexible and dynamic.
# - It allows the method to work with subclasses in the case of inheritance, 
#   since 'cls' will always refer to the calling class, which could be a subclass in the inheritance hierarchy.

# In class methods, 'cls' can be used to:
# 1. Access or modify class-level variables (those shared across all instances).
# 2. Instantiate objects of the class (via 'cls' instead of using the class name directly).
# 3. Implement logic that works at the class level, as opposed to the instance level.

# 'cls' vs 'self':
# - 'self' refers to the current object (instance) and is used to access or modify instance variables.
# - 'cls' refers to the class itself and is used to access or modify class variables, or to instantiate objects using class-level methods.
