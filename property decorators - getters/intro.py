class institution:
    # The constructor (__init__) initializes the class with course price and course name
    def __init__(self, course_price, course_name):
        self.__course_price = course_price  # A private attribute (__course_price)
        self.course_name = course_name  # A public attribute (course_name)

    # Property decorator to access the private attribute __course_price
    @property
    def coursse_price_access(self):
        return self.__course_price  # Accessor for __course_price

    # Setter to modify the __course_price attribute
    @coursse_price_access.setter
    def course_price_set(self, price):
        # Only set the price if it's greater than 3500
        if price <= 3500:
            pass  # Don't change the price if it's less than or equal to 3500
        else:
            self.__course_price = price  # Otherwise, update the price

    # Deleter to delete the __course_price attribute
    @coursse_price_access.deleter   
    def del_course_price(self):
        del self.__course_price  # Deletes the __course_price attribute

# Creating an instance of the institution class
obj = institution(3500, "dsa")

# Accessing the course price using the property method
print(obj.coursse_price_access)  # Output: 3500

# Setting a new value for the course price using the setter method
obj.course_price_set = 4500
print(obj.coursse_price_access)  # Output: 4500

# Deleting the course price using the deleter method
del obj.del_course_price
# print(obj.coursse_price_access)  # Uncommenting this would raise an error as the course price is deleted
