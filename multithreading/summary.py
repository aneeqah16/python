# What is Threading?

# Threading is a way to divide a task into smaller parts, called threads, that can run independently. A thread is the smallest unit of execution within a program. Instead of waiting for one task to finish before starting another, threads allow multiple tasks to run at the same time. This helps make programs faster and more efficient, as different tasks can be handled at once.

# What is Multithreading?

# Multithreading is a technique that allows a program to run multiple threads at the same time. This helps to make better use of the computer's processing power. For example, if a computer has four cores (like a quad-core processor), each core can handle a different thread at the same time. If there are more threads than cores, the threads will be switched quickly between the cores, giving the appearance that they are running at the same time.


# In simpler terms, multithreading lets a program do several tasks at once, which can save time and make the program run more efficiently. For example, while one thread is waiting for some data from the internet, another thread can perform a different task without waiting.

# How Multithreading Works

# In multithreading, each thread works independently but shares the same memory space with other threads in the same program. This means that while each thread has its own set of instructions and local variables, all threads can access the same data in memory. This makes threads lightweight and faster to create compared to processes, which would require separate memory.

# Each thread has its own stack (for storing temporary data), registers (for small pieces of data), and program counter (for keeping track of the next instruction to execute). However, all threads share the same global memory space.
# How to Start a Thread in Python?

# In Python, multithreading is easy to use with the threading module. You can create a new thread by defining a function for the thread to run. Then, you create a thread object and use the start() method to run the thread.
# example 
import threading
import time

# A function that the thread will run
def print_numbers():
    for i in range(5):
        print(i)

# Creating a thread object and starting it
thread = threading.Thread(target=print_numbers)
thread.start()

# Wait for the thread to finish
thread.join()

# How the sleep() Function Works

# In multithreading, the sleep() function is often used to pause the execution of a thread for a specific amount of time. This can be useful when you want to delay certain actions or prevent threads from using too much CPU time when they don't need to do anything.

# For example, if a thread needs to wait for some data or perform an action after a delay, you can use sleep() to pause it temporarily. The rest of the threads in the program can continue running while the paused thread waits.

# example:


# A function that the thread will run
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)  # Pauses the thread for 1 second

# Creating a thread object and starting it
thread = threading.Thread(target=print_numbers)
thread.start()

# Wait for the thread to finish
thread.join()

# The sleep() function helps control the timing of threads, allowing them to pause and resume without blocking other threads from running.


# Lock and Shared Variables

# When using multithreading, shared variables are variables that are used by more than one thread. Since multiple threads can access and modify these variables at the same time, it can lead to problems like race conditions (where the result depends on the order in which threads are executed).

# For example, if two threads try to update the same variable at the same time, the final value of the variable may not be correct because both threads might overwrite each other’s changes.

# To avoid this, we use a lock. A lock is a synchronization tool that helps manage access to shared variables. When one thread locks a resource, other threads have to wait until the lock is released before they can access it.

# example:
# Shared variable
counter = 0

# Create a lock object
lock = threading.Lock()

# A function that the thread will run
def increment():
    global counter  # Use the shared global variable
    for _ in range(10):  # Loop to increment the counter 1000 times
        lock.acquire()  # Acquire the lock before modifying the shared resource (counter)
        
        # The lock ensures that only one thread can enter this section of code at a time
        counter += 1  # Increment the counter
        
        lock.release()  # Release the lock so other threads can acquire it

# Creating two threads that will both call the increment function
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Starting both threads to run the increment function
thread1.start()
thread2.start()

# Wait for both threads to finish their work
thread1.join()
thread2.join()

# Print the final value of the counter
print("Counter:", counter)


