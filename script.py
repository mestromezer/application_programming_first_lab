from msilib.schema import File
import requests
from bs4 import BeautifulSoup as BS
import sys
sys.getdefaultencoding()
'ascii'
sys.getfilesystemencoding()
'UTF-8'
import os
import time
        
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
    
def create_repo():
    os.rmdir("dataset")
    os.mkdir("dataset")
    for i in range(1,6):
        os.mkdir("dataset/"+str(i))
        
def get_page(url):
    r = requests.post(url,headers={"User-Agent":"Mozilla/5.0"})
    #print(r.text)
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
    
    html = get_page(url)
    
    if html == -1 : 
            print("No connection")
            exit()
            
    for i in range (1,9999):
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
            condidate = {names[j]:[comments[j],marks[j]]}
            if condidate[names[j]][1] < 1 : 
                zero+=1
                dataset.update(condidate)
            elif condidate[names[j]][1] < 2 : 
                one+=1
                dataset.update(condidate)
            elif condidate[names[j]][1] < 3 : 
                two+=1
                dataset.update(condidate)
            elif condidate[names[j]][1] < 4 : 
                three+=1
                dataset.update(condidate)
            elif condidate[names[j]][1] < 5 : 
                four+=1
                dataset.update(condidate)
            elif condidate[names[j]][1] == 5 : 
                five+=1
                dataset.update(condidate)
    
    """
    print(marks)
    
    print(names)
    
    outFile = open('output.xml', 'wb')
    for comment in comments:
        outFile.write(comment.encode('utf-8'))
        outFile.write('\n\n\n'.encode('utf-8'))
    """
    
    
    
            
    
        
