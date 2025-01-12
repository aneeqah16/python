import threading
import urllib.request
# creating a target function
def file_download(url,filename):
    urllib.request.urlretrieve(url, filename)


url_list = ["https://gist.githubusercontent.com/apipemc/6047552/raw/5cf8793e00d569de4f1ee8c125648ee5e0b6e2de/links.txt","https://raw.githubusercontent.com/dominictarr/random-name/refs/heads/master/first-names.txt","https://raw.githubusercontent.com/ProHiryu/flower-recognition/refs/heads/master/flowers.txt"]
# here we are creating a list of urls to download from


file_name_list = ["data1.txt","data2.txt","data3.txt"]
# here we are creating a list of file names to be used later

#  now we are creating a thread for each url in the list


tread = [threading.Thread(target=file_download, args=(url_list[i], file_name_list[i])) for i in range(len(url_list))]
# here we created a list of threads

print(tread)
# it shows it will create 3 threads of file_download that is basically a function that downloads a file from a url
# now we are starting the threads
for i in range(len(tread)):
    tread[i].start()

# here we used for loop to start each thread in the list


