# threading is basically a way to run multiple threads in a program
# threads are like processes but they share the same memory space
# Basically, a quad-core processor is a type of computer chip that has four separate units (cores) inside it, allowing it to handle multiple tasks at the same time. This makes the computer faster and more efficient when running several programs. Multithreading is a way for a single program to do different things at once by using smaller parts called threads. Even if there are more threads than cores, the computer can quickly switch between them, making it seem like everything is running smoothly at the same time. This helps improve the overall performance of the computer, especially when it has to wait for things like downloading files.
import threading
import urllib.request
def test(id):
    print(f"Thread {id} is running")


test(45)
thread =  [threading.Thread(target = test,args=(i,)) for i in range(10)]
# this program will run 10 threads
# it will create 10 threads in one core and run them one by one
for t in thread:
    t.start()
print(list(thread))
print(id(thread))


url_list = ["https://gist.githubusercontent.com/apipemc/6047552/raw/5cf8793e00d569de4f1ee8c125648ee5e0b6e2de/links.txt","https://raw.githubusercontent.com/dominictarr/random-name/refs/heads/master/first-names.txt","https://raw.githubusercontent.com/ProHiryu/flower-recognition/refs/heads/master/flowers.txt"]
