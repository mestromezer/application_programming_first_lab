import requests
from bs4 import BeautifulSoup as BS
import sys
import os
import re
# -*- coding: cp1251 -*-

class FileManager:
    def __init__(self, name, mode):
        self.file = open(name, mode)
        self.stdout = sys.stdout

    def __del__(self):
        self.close()

    def write(self, data):
        self.stdout.write(data)
        self.file.write(data)

    def flush(self):
        self.stdout.flush()
        self.file.flush()

    def close(self):
        if sys.stdout is self:
            sys.stdout = self.stdout
        self.file.close()
    
def create_repo():
    os.rmdir("dataset")
    os.mkdir("dataset")
    for i in range(1,6):
        os.mkdir("dataset/"+str(i))

def set_connection(url):
    r = requests.post(url,headers={"User-Agent":"Mozilla/5.0"})
    print(r.status_code)
    if r.status_code == 200:
        return r.text
    else:
        return 0
    
def urls_to_comments(soup):
    return soup.find_all('a','class'=='review-btn review-read-link')
        
        
        
if __name__=="__main__":
    url = input("Укажите URL: ")
    content = set_connection(url)
    soup = BS(content)
    urls = urls_to_comments(soup)
    print(urls)
