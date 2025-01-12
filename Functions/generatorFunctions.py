# Range function example
print(range(0, 12))

# Iterating over the range using a for loop
for i in range(0, 10):
    print(i)

# Why do we use generator functions?

# Generator functions are used to reduce memory consumption because they generate each element one by one
# without storing all the elements in memory at once.

def test_fib(n):
    a, b = 0, 1  # Initializing first two Fibonacci numbers
    for i in range(n):
        yield a  # Yielding each Fibonacci number one at a time
        a, b = b, a + b  # Calculating the next Fibonacci number

# Calling the generator function directly prints the generator object
print(test_fib(10))  # It prints the generator object itself

# Iterating over the generator function to get the Fibonacci numbers one by one
for i in test_fib(10):
    print(i)

# Example with string iteration
s = "aneeqah"

# Iterating over the string and printing each character
for i in s:
    print(i)

print(s)  # Printing the whole string

# The 'next' function does not work on a string directly:
# print(next(s))  # This will give an error: 'str' object is not an iterator

# Strings are iterable but not iterators. To make a string an iterator, we use the 'iter' function.

s1 = iter(s)  # Converting the string to an iterator
print(type(s1))  # Type of s1 will be <class 'iterator'>

# Now we can use 'next' on the string iterator
print(next(s1))  # Prints first character 'a'
print(next(s1))  # Prints second character 'n'
print(next(s1))  # Prints third character 'e'
print(next(s1))  # Prints fourth character 'e'
print(next(s1))  # Prints fifth character 'q'
print(next(s1))  # Prints sixth character 'a'
print(next(s1))  # Prints seventh character 'h'

# Explanation:
# The for loop internally calls 'iter' to create an iterator and then uses 'next' to iterate over the items
# The loop knows when to stop because it automatically checks if all items have been exhausted (length of the iterable).

# Can we convert a number to an iterable?
# No, integers cannot be made into iterables directly.

# Example (this will give an error):
# n = iter(45)  # TypeError: 'int' object is not iterable

# Only objects that are iterable (like strings, lists, tuples) can be converted into iterators.

# Summary:
# - An "iterable" is any object that can be converted to an iterator (i.e., can be traversed over).
# - An "iterator" is an object that produces the next value on each call to 'next()' and keeps track of the current position.
