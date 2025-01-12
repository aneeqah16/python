import time

# A simple function to test the output and logic
def test():
    print("This is the start of the function.")
    print("This is my function to test.")
    print(4 + 5)
    print("This is the end of the function.")

# Uncomment the line below to call the function 'test'
# print(test())


# Decorator function that adds extra functionality before and after the execution of the original function
def deco(func):
    def inner_dec():
        print("This is the start of the function.")
        func()  # This calls the original function
        print("This is the end of the function.")
    return inner_dec  # The decorator returns the inner function

# Applying the decorator using '@deco', which means we are calling 'deco(test1)'
# This will execute 'deco' and then pass the 'test1' function as an argument to 'deco'
@deco
def test1():
    print(6 + 7)

# Calling test1 now will first run the code inside 'deco' before running 'test1'
test1()


# A timer decorator to measure how long a function takes to execute
def timer_test(func):
    def timer_test_inner():
        start = time.time()  # Store the time before calling the function
        func()  # Execute the original function
        end = time.time()  # Store the time after the function has executed
        print("Execution time:", end - start, "seconds")  # Print the execution time
    return timer_test_inner  # Return the inner function which will be used as the decorated version of 'test2'


# Applying the 'timer_test' decorator to 'test2'
@timer_test
def test2():
    print(45 + 78)

# Calling 'test2' will now show the time it took to execute the function
print("-------------------")
test2()


# Testing with a larger function to see the effect of the timer
@timer_test
def test4():
    for i in range(100000000):  # A loop that runs for a large number of iterations
        pass  # Doing nothing, just looping to waste time

# Calling 'test4' will show the time taken by this loop to execute
test4()
