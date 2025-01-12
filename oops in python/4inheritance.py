# inhertance:

class test : 
    def test_meth(self):
        return "this is my first class"
    
class child_test(test):
    def child_meth(self):
        return "this is a child meth"

child_test_obj = child_test()

print(child_test_obj.test_meth())
print(child_test_obj.child_meth())
# multi level inheritance:
class class1:

    def test_class1(self):
        return "this is a meth from class1"
    
class class2(class1):
    # inheriting class1

    def test_class2(self):
        return "this is a meth from class2"
    
class class3(class2):
    pass

cl3_obj = class3()
print(cl3_obj.test_class1() )
print(cl3_obj.test_class2())
# Multilevel Inheritance in Python is a type of Inheritance in which a class inherits from a class, which itself inherits from another class. 

# multiple inheritance
# When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.

class class1:
    def test_class1(self):
        return "this is a class1"
    
class class2:
    def test_class2(self):
        return "this is class2"
    
class class3(class1,class2):
    # class3 inheriting both class1 and class2
    def test_class3(self):
        return "this is class3"
    
obj_class3 = class3()
print(obj_class3.test_class1())
print(obj_class3.test_class2())
print(obj_class3.test_class3())