n = 3
p = 2

def test(n,p):
    return n**p

print(test(n,p))

# but instead of writing code in 2 or more lines we can use lambda function for them


a = lambda n,p : n**p
print(a(3,2))
# here we call it lambda function, one liner function, anonymous function

add = lambda x,y: x+y

print(add(5,7))

c_to_f = lambda c:(9/5)*c +32
print(c_to_f(45))

# finding the max of two numbers using the lambda function

max_number = lambda x,y :x if x>y else y
print(max_number(7,8))

# write a lambda function to return the length of a string

len_of_string = lambda s1: len(s1)

print(len_of_string("Aneeqah"))
print(len_of_string("Aisha"))