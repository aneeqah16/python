# multiprocessing : 
#   - multiprocessing is a module that allows you to spawn new Python processes.
#   - It is a more powerful and flexible way to run tasks in parallel than threading.

# it means enagaing multiple processor to exrcute multiple programs and to establish communication between them.
import multiprocessing

def test():
    print("This is my multiprocessing program ")
if __name__ == "__main__":
    # this is the main program that invokes all the resources, interpreter, compliler , etc.
    m = multiprocessing.Process(target = test)
    # this means that after the execution of the main then the test function will be executed
    print("This is my main program ")

    # the program will execute the test function when we use start function 
    m.start()
    # this is used to stop the execution of the program
    m.join()
print("--------------------------")
# test()