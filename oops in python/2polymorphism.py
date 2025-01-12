# polymorphism: different kinds of behaviour in different situations
def test(a,b):
    return a+b

print(test(4,4))
# passing strings
print(test("aneeqah","ashraf"))
# nature differnt in different context

# passing lists
print(test([1,2,3],[4,5,6]))


class Data_science:

    def syllabus(self):
        print("this my syllabus for data science masters")


class Web_dev:
    
    def syllabus(self):
        print("this is my syllabus for web dev")


def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()


ds = Data_science()
wd = Web_dev()
class_obj = [ds,wd]
class_parcer(class_obj)   
        