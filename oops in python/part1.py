# oops stands for Object_oriented programming system

a =1

print(type(a))
# <class 'int'>

# what is a class:
# class is a blueprint or the skeleton or defines objects in oops
# object is the real world entity also known as instance 


#  how to create a class in python
#  with a class keyword
class test:
    pass

# why do we create a class in the programming 
# brings structure and reusibility in code

#  how to create an object of the class
a = test()
print(type(a))

# creating a random class

class skills:
    #  creating a method/function
    def Welcome_message():
        print("welcome")

person1 = skills()
print(type(person1))
# <class '__main__.skills'>

# person1.Welcome_message()
# TypeError: skills.Welcome_message() takes 0 positional arguments but 1 was given

# reason: whatever function we write in the class should have been binded with the class and that is done using the self keyword
class skills:
    #  creating a method/function
    def Welcome_message(self):
        print("welcome")

person2 = skills()
#  here person is an instance of the class skills
print(type(person2))
person3 = skills()
person3.Welcome_message()


class skills1 :
    # To pass object specific  data to the class we use an inbuilt function __init__() also known as constructor
    def __init__(self,name,phone_number,email_id,student_id):
       self.name = name
    #    self.name belongs to class/ self binds it to the  class
    # self is not a reserved keyword, we can use any other word instead of self that behaves a pointer
       self.phone_number = phone_number
    #    self.phone_number belongs to class
       self.email_id= email_id
    #    self.emailid belongs to class
       self.student_id = student_id
    #    self.email_id belongs  to class

    def student_Details(self):
        print(f"The name is : {self.name}, email is : {self.email_id}, phone number is : {self.phone_number}, student_id is : {self.student_id}")


Aneeqah = skills1("Aneeqah",9787868567,"aneeqah@ashraf",23550034)
Aneeqah.student_Details()

eman = skills1("Eman",68775878656,"eman@zaffar",8776)
eman.student_Details()
print(eman.email_id)





