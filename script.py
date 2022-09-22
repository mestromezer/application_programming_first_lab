from base64 import encode
from msilib.schema import File
import requests
from bs4 import BeautifulSoup as BS
import os
import time

class Comment:
    
    def __init__(self,name,comment,mark):
        if name != '': self.name = name
        if comment!='': self.comment = comment
        if mark<=5 and mark >= 0: self.mark = mark
    def get_mark(self): return self.mark
    def get_name(self): return self.name
    def get_comment(self): return self.comment
        
headers = {
    'User-Agent':'Mozilla/5.0'
}

def create_repo():
    os.mkdir("dataset")
    for i in range(0,6):
        os.mkdir("dataset/"+str(i))
        
def get_page(url):
    r = requests.get(url,headers=headers)
    time.sleep(3)
    if(r.status_code == 200) : return BS(r.content,'html.parser')
    else : 
        print("No connection")
        exit()
    
def get_marks(items):
    marks = list()
    for item in items:
            marks.append(float(item.text.strip()))
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
    
def save_comments(data, filename):
    for i in range(1,len(data)):
        file = open(filename+f'\\{i:04}'+'.txt', "w", encoding="utf-8")
        file.write(data[i].name)
        file.write('\n')
        file.write(data[i].comment)
        file.close
        
def parse_pages(max_num_of_requests, least_num_of_marks):
    dataset = list()
    zero=0
    one=0
    two=0
    three=0
    four=0
    five=0
    for i in range (1,max_num_of_requests):
        
        if zero>=least_num_of_marks and one>=least_num_of_marks and two>=least_num_of_marks and three>=least_num_of_marks and four>=least_num_of_marks and five>=least_num_of_marks: #!!! one < least..
            i=max_num_of_requests
            break
        
        html = get_page(url+'~'+str(i)+'#reviews')
        if html == -1 : break
        
        marks = get_marks(html.findAll('span',class_='lenta-card__mymark'))
        
        names = get_names(html.findAll('a', class_='lenta-card__book-title'))
        
        comments = get_comments(html.findAll('div',id='lenta-card__text-review-escaped'))
            
        for j in range(marks.__len__()):
            condidate = Comment(names[j],comments[j],marks[j])
            
            if condidate.mark < 1: 
                zero+=1
            
            if condidate.mark < 2.0 : 
                one+=1
                
            elif condidate.mark < 3.0 : 
                two+=1
                
            elif condidate.mark < 4.0 : 
                three+=1
                
            elif condidate.mark < 5.0 : 
                four+=1
                
            elif condidate.mark == 5.0 : 
                five+=1
            
            dataset.append(condidate)
    return dataset
    
    
if __name__=="__main__":
    
    url = 'https://www.livelib.ru/reviews/'
    
    least_num_of_marks = 100
    max_num_of_requests = 700
    
    get_page(url) #check connection
            
    dataset = parse_pages(max_num_of_requests, least_num_of_marks)
    
    create_repo()
    
    #dataset.sort(key = lambda comment: comment.mark)
    
    zero_data = [el for el in dataset if el.get_mark() < 1.0]
    print(zero_data)
    save_comments(zero_data,'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\0')
    
    one_data = [el for el in dataset if el.get_mark()<2.0 and el.get_mark()>=1.0]
    save_comments(one_data,'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\1')
    
    two_data = [el for el in dataset if el.get_mark()<3.0 and el.get_mark()>=2.0]
    save_comments(two_data,'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\2')
    
    three_data = [el for el in dataset if el.get_mark()<4.0 and el.get_mark()>=3.0]
    save_comments(three_data,'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\3')
    
    four_data = [el for el in dataset if el.get_mark()<5.0 and el.get_mark()>=4.0]
    save_comments(four_data,'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\4')
    
    five_data = [el for el in dataset if el.get_mark()==5.0]
    save_comments(five_data,'C:\\Users\\RELOAD\\Desktop\\Уник\\прикладное пр-е\\FirstLabParser\\Application-programming\\dataset\\5')
    
    
        
