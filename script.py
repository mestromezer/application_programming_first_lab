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
<<<<<<< HEAD
        if mark<=5 and mark >= 0: self.mark = int(mark)
    
    def get_mark(self): return self.mark
=======
        if mark<=5 and mark > 0: self.mark = mark
>>>>>>> 529bcf81bb3acc3244d8bfcf22b38c3839e60b1a
    
    def print_values(self):
        print(f"Name:{self.name}\nMark: {self.mark}\nComment: {self.comment}")
        
headers = {
    'accept': '*/*',
<<<<<<< HEAD
    'User-Agent':'Mozilla/5.0'
=======
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
>>>>>>> 529bcf81bb3acc3244d8bfcf22b38c3839e60b1a
}
    
def create_repo():
    os.mkdir("dataset")
    for i in range(1,6):
        os.mkdir("dataset/"+str(i))
        
def get_page(url):
    r = requests.get(url,headers=headers)
<<<<<<< HEAD
=======
    print(r.text)
>>>>>>> 529bcf81bb3acc3244d8bfcf22b38c3839e60b1a
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
    
<<<<<<< HEAD
=======
    least_num_of_marks = 2
    
    max_num_of_requests = 5
    
>>>>>>> 529bcf81bb3acc3244d8bfcf22b38c3839e60b1a
    html = get_page(url)
    if html == -1 : 
            print("No connection")
            exit()
            
    for i in range (1,max_num_of_requests):
<<<<<<< HEAD
        
        if one>=least_num_of_marks and two>=least_num_of_marks and three>=least_num_of_marks and four>=least_num_of_marks and five>=least_num_of_marks: 
            i=max_num_of_requests
        
        html = get_page(url+'~'+str(i)+'#reviews')
        if html == -1 : break
        
        marks = get_marks(html.findAll('span',class_='lenta-card__mymark'))
=======
        
        if one>least_num_of_marks and two>least_num_of_marks and three>least_num_of_marks and four>least_num_of_marks and five>least_num_of_marks: 
            i=max_num_of_requests
        
        html = get_page(url+'~'+str(i)+'#reviews')
        
        if html == -1 : break
>>>>>>> 529bcf81bb3acc3244d8bfcf22b38c3839e60b1a
        
        names = get_names(html.findAll('a', class_='lenta-card__book-title'))
        
        comments = get_comments(html.findAll('div',id='lenta-card__text-review-escaped'))
            
        for j in range(marks.__len__()):
<<<<<<< HEAD
            condidate = Comment(names[j],comments[j],float(marks[j]))
=======
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
    
    
    
>>>>>>> 529bcf81bb3acc3244d8bfcf22b38c3839e60b1a
            
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
    
    dataset.sorted(dataset, key = lambda comment: comment.get_mark())
    
    for elem in dataset:
        elem.print_value()
        print('\n'*3)
    
    for comment in dataset:
        filename = 'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\'+str(comment.mark[0])
        file = open(filename,'wb+')
        get_last_file_name(filename)
        
        file.close()
