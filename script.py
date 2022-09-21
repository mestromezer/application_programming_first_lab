from msilib.schema import File
import requests
from bs4 import BeautifulSoup as BS
import sys
import os
import time

class Comment:
    
    def __init__(self,name,comment,mark):
        if name != '': self.name = name
        if comment!='': self.comment = comment
        if mark<=5 and mark > 0: self.mark = mark
    
    def print_values(self):
        print(f"Name:{self.name}\nMark: {self.mark}\nComment: {self.comment}")
        
headers = {
    'accept': '*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
    
def create_repo():
    os.rmdir("dataset")
    os.mkdir("dataset")
    for i in range(1,6):
        os.mkdir("dataset/"+str(i))
        
def get_page(url):
    r = requests.get(url,headers=headers)
    print(r.text)
    time.sleep(3)
    if(r.status_code == 200) : return BS(r.content,'html.parser')
    else : return -1

if __name__=="__main__":
    
    url = 'https://www.livelib.ru/reviews/'
    
    dataset = dict()
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    
    least_num_of_marks = 2
    
    max_num_of_requests = 5
    
    html = get_page(url)
    if html == -1 : 
            print("No connection")
            exit()
            
    for i in range (1,max_num_of_requests):
        
        if one>least_num_of_marks and two>least_num_of_marks and three>least_num_of_marks and four>least_num_of_marks and five>least_num_of_marks: 
            i=max_num_of_requests
        
        html = get_page(url+'~'+str(i)+'#reviews')
        
        if html == -1 : break
        
        marks = list()
    
        for item in html.findAll('span',class_='lenta-card__mymark'):
            marks.append(item.text.strip())
        
        names = list()
    
        for item in html.findAll('a', class_='lenta-card__book-title'):
            names.append(item.text.strip())
        
        comments = list()
    
        for item in html.findAll('div',id='lenta-card__text-review-escaped'):
            comments.append(item.text.strip())
            
        for j in range(marks.__len__()):
            condidate = Comment(names[j],comments[j],marks[j])
            
            if condidate.mark < 1.0 : 
                zero+=1
                dataset.update(condidate)
                
            elif condidate.mark < 2.0 : 
                one+=1
                dataset.update(condidate)
                
            elif condidate.mark < 3.0 : 
                two+=1
                dataset.update(condidate)
                
            elif condidate.mark < 4.0 : 
                three+=1
                dataset.update(condidate)
                
            elif condidate.mark < 5.0 : 
                four+=1
                dataset.update(condidate)
                
            elif condidate.mark == 5.0 : 
                five+=1
                dataset.update(condidate)
        
    print(f"Parsed:\none: {one}\ntwo: {two}\nthree: {three}\nfour: {four}\nfive: {five}")
    
    """
    print(marks)
    
    print(names)
    
    outFile = open('output.xml', 'wb')
    for comment in comments:
        outFile.write(comment.encode('utf-8'))
        outFile.write('\n\n\n'.encode('utf-8'))
    """
    
    
    
            
    
        
