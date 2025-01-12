import threading 
import urllib.request
import time

shared_var = 0
#  this is a shared variable which will be accessed by multiple threads
lock_var = threading.Lock()
#  this is a lock which will be used to prevent race conditions

def test2(id):
    global shared_var 
    # all threads will be accessing the shared variable and will be printing some values 
    with lock_var :
        shared_var= shared_var+1
        print(f"test2 id is {id}  has incresed the shared variable by {shared_var}")
        time.sleep(1)

thre3 = [threading.Thread(target=test2,args=(i,)) for i in range(3)]
#  creating 3 threads which will be calling the test2 function with different id's
for thread in thre3:
    thread.start()
    #  starting all the threads

