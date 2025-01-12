# abstraction: 
# used to create a skeleton
import abc
class Student:
    @abc.abstractmethod
    def student_details(self):
        pass
    @abc.abstractmethod
    def student_assignment(self):
        pass
    @abc.abstractmethod
    def student_marks(self):
        pass

class student_details(Student):
    def student_details(self):
        return "this is a method for taking student details"
    
    def student_assignment(self):
        return "this is a method for assigning details for a particular student "
    
class ds(Student):
    def student_details(self):
        return 'this will return student detaails for ds'
    def student_assignment(self):
        return "this will return details for assignment in ds"
    
dsm = ds()
print(dsm.student_details())
