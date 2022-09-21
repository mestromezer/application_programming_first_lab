from fileinput import filename
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
        if mark<=5 and mark >= 0: self.mark = mark
    
    def print_values(self):
        print(f"Name:{self.name}\nMark: {self.mark}\nComment: {self.comment}")
        
headers = {
    'accept': '*/*',
    'User-Agent':'Mozilla/5.0'
}
    
def create_repo():
    os.mkdir("dataset")
    for i in range(1,6):
        os.mkdir("dataset/"+str(i))
        
def get_page(url):
    r = requests.get(url,headers=headers)
    time.sleep(3)
    if(r.status_code == 200) : return BS(r.content,'html.parser')
    else : return -1
    
def get_marks(items):
    marks = list()
    for item in items:
            marks.append(item.text.strip())
    return marks

def get_names(items):
    names = list()
    for item in items:
        names.append(item.text.strip())
    return names
        
def get_comments(items):
    comments = list()
    for item in items:
        comments.append(item.text.strip())
    return comments
        
def get_last_file_name(path):
    files = os.listdir(path)
    if files: return files[files.__len__()]
    
if __name__=="__main__":
    
    url = 'https://www.livelib.ru/reviews/'
    
    dataset = list()
    one=0
    two=0
    three=0
    four=0
    five=0
    
    least_num_of_marks = 1
    max_num_of_requests = 7000
    
    html = get_page(url)
    if html == -1 : 
            print("No connection")
            exit()
            
    for i in range (1,max_num_of_requests):
        
        if one>=least_num_of_marks and two>=least_num_of_marks and three>=least_num_of_marks and four>=least_num_of_marks and five>=least_num_of_marks: 
            i=max_num_of_requests
        
        html = get_page(url+'~'+str(i)+'#reviews')
        if html == -1 : break
        
        marks = get_marks(html.findAll('span',class_='lenta-card__mymark'))
        
        names = get_names(html.findAll('a', class_='lenta-card__book-title'))
        
        comments = get_comments(html.findAll('div',id='lenta-card__text-review-escaped'))
            
        for j in range(marks.__len__()):
            condidate = Comment(names[j],comments[j],float(marks[j]))
            
            if condidate.mark <= 1.0 : 
                one+=1
                dataset.append(condidate)
                
            elif condidate.mark <= 2.0 : 
                two+=1
                dataset.append(condidate)
                
            elif condidate.mark <= 3.0 : 
                three+=1
                dataset.append(condidate)
                
            elif condidate.mark <= 4.0 : 
                four+=1
                dataset.append(condidate)
                
            elif condidate.mark <= 5.0 : 
                five+=1
                dataset.append(condidate)
    
    create_repo()
    
    counter = 0
    
    for comment in dataset:
        filename = 'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\'+str(comment.mark[0])
        file = open(filename,'wb+')
        get_last_file_name(filename)
        
        file.close()
