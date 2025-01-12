import threading
import urllib.request

def file_download(url,filename):
    urllib.request.urlretrieve(url, filename)

file_download("https://gist.githubusercontent.com/apipemc/6047552/raw/5cf8793e00d569de4f1ee8c125648ee5e0b6e2de/links.txt","text.txt")
# this will download the file from the given url and save it as text.txt in the current directory.
