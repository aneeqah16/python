import threading 
import urllib.request
import time


def test1(id):
    for i in range(10):
        print("test1 %d printing %d %s"%(id,i,time.ctime()))
        time.sleep(1)
        # sleeps for 1 second
#  this function will be doing some task and will be printing some values
#  it will be running in a separate thread

# print(test1(0))

thread1 = [threading.Thread(target=test1, args=(i,))for i in range(3)]

for t in thread1:
    t.start()

# import threading 
# import urllib.request
# import time

# def test1(id):
#     for i in range(10):
#         print(f"test1 {id} printing {i} {time.ctime()}")
#         time.sleep(1)

# def main():
#     thread1 = [threading.Thread(target=test1, args=(i,)) for i in range(3)]

#     for t in thread1:
#         t.start()

#     for t in thread1:
#         t.join()

# if __name__ == "__main__":
#     main()