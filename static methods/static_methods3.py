class institution2:
    # different copies for different objects
    def student_details(self,name,emailid,number):
        print(name,emailid,number)

    # static method decorator
    @staticmethod #this method can be accessed without creating the objects
    # also used to create utilities/ utilities functions
    # same copy shared by all th objects
    def mentor_class(list_mentor):
        print(list_mentor)
    # calling one static method into another static method
    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        institution2.mentor_class(["anee","haami","eman","irtiza"])
        print(mail_id_mentor)

    @classmethod
    def class_name(cls):
        # using static method inside a class method
        cls.mentor_class(["ghkhgf","fghj"])

    def mentor(self,mentor_list):
        print(mentor_list)
        # calling static method in the instance class
        self.mentor_class(["anee","haami"])

institution2.class_name()
institution2.mentor_mail_id(["anee@gmail.com","haami@gmail.com","eman@gmail.com","irtiza@gmail.com"])
obj1 = institution2()
obj1.mentor(["eman","iriza"])

# how to achieve memory optimization in classes
# ans: using static methods
#what is a static method
# a method that can be accessed without creating the objects and is bound to the class 

# what is the difference between static and class method

# both are bound to the class rather than the instance of the class but :
# the purpose of the class method is that it is often used for alternative constructors(overloading), factory methods, or operations that need to access the class itself, furthermore it takes cls as its first argument representating the class itself

# the purpose of the static method is that it is used for the utility functions that are logically related to the class but dont need to access the class or instance state
# cannot access or modify instance or class-level variables directly 

# 



    