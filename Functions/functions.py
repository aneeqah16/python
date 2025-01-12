#  creating a function

def test():
    print("This is my first function")
    #  lag raha hai yeh string hain lekin yeh stirng nahi hai
    # yeh non type hai 

    # print always return none data type

test()
# reusiblity increase 

# test() + "Aneeqah"
# we dont use print in function return 
# instead we use return keyword


def test2():
    return "this is my very first return"

print(test2())
# now we can concatnate
print(test2() + " aneeqah")

def test3():
    return "aneeqah",34,4564.45,[1,2,3,5,5]
# return in the form of tuples

print(test3())

a,b,c,d = test3()
print(test3())
print(a)
print(b)
print(c)
print(d)

# same as a,b = 1,4

def test4():
    a = 5 + 6 / 7
    return a 

print(test4())

def test5(a,b,c):
    d = a+b/c
    return d

print(test5(5,7,7))


def test6(a,b):
    return a+b

print(test6(8,6))
print(test6("anee","qah"))
print(test6([6,7,84,4],[2,5,6,7,8]))

l = [1,2,3,4,"anee","qah",[1,2,3,4,5,6]]

l1 = []
for i in l :
    if type(i) == int or type(i)==float:
        l1.append(i)

print(l1)

def test7(l):
    l1 = []
    for i in l :
        if type(i) == int or type(i)==float:
            l1.append(i)

    return l1

print(test7([1,23,5,6,34,564,5]))

def test8(l):
    """This is my function to extract num data from list"""
    l2 = list()
    for i in l:
        if type(i) == list:
            for j in i:
                l2.append(j)
        else:
            if type(i)== int or type(i) == float:
                l2.append(i)

    return l2


print(f"the list is {test8(l)}")

def test10(a,b):
    return a+b

# dynamic arguments

def test11(*args):
    return args

print(type(test11()))

print(test11(1,2,3,4,5))
print(test11(1,2,3,4,5,56,76,453,567,453,4,"aneeqah","ashraf",[556,343,34,5]))
# prints in the form of tuples

# args here is not a keyword
# * helps to take multiple user input 

def test13(*args, a):
    return args, a

   # error as the interpreter gets comfused from where the first muliple arugmument variables ends up taking up the inputs

# to fix this issue we have can do :

print(test13(1,2,3,4,5, a = 23))

def test14(c,d,a = 23 , b = 1):
    return a, b,c ,d

print(test14(3,4))
print(test14(3,4, a = 34343))
print(test14(3,4, a = 34343, b =4534))

def test15(**kwargs):
    # takes key and value pair as argument
    return kwargs

print(test15())
print(test15(a= [12,53,353,323], b = "Aneeqah", c = 34242.5643))
# gives us the dictonary as the result 
