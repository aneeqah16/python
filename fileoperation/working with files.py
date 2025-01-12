import os
import shutil
# f = open("test.txt","w")
# # open is an in built function that is used to perform operations on files
# f.write("this is my first file to write")
# f.close()


# f = open("test.txt","w")
# f.write("this is file to write")
# f.close()

# f = open("test.txt","a")
# f.write("this is file to write gjk Note: Since Cube class does not have an __init__() method, the __init__() of Square class will be used for initialization of Cube instances (basic property of inheritance). Considering this example, we know that each face of a cube is a square and hence, face_area of Cube represents area of a Square. Now, it makes sense to evaluate face_area using area() method of the class Square rather than calculating it manually, not only this will save us from rewriting the code but also it will allow to change the area() logic from one place. But as we have overridden the area() method in Cube, we cannot call area() method of Square using self.area(). Now, this is a situation where super() comes in rescue. super() returns a proxy object of the parent class and then you call the method of your choice on that proxy object, thus, we can call the area() method of Square class")
# f.close()


data = open("test.txt","r")
# data.read()
print(data.read())
# read line by line 
# data.readline()
data.seek(0)
print(data.readline())

data1 = open("test.txt","r")
for i in data1:
    print(i)


# print(os.path.getsize("test.txt"))

# os.remove("test.txt")
# os.rename("test.txt","new.txt")
shutil.copy("test.txt","copy_new.txt")
with open("new.txt","a") as f:
    f.write("hjkxcvbnjk ghjuytrdtdxcfgvhbj vghbjkiuytdfg vbhnjkhfdcvb ghjkjvhcfgh")
    print(f.read())