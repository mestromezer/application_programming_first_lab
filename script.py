from base64 import encode
from msilib.schema import File
import requests
from bs4 import BeautifulSoup as BS
import os
import time
#import HAND_MADE_PROXY

class Comment:
    
    def __init__(self,name,comment,mark):
        if name != '': self.name = name
        if name == None: 
            print('Некорректное название')
            exit()
        if comment == None: 
            print('Некоррректное содержимое комментария')
            exit()
        self.comment = comment
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
    time.sleep(3)
    r = requests.get(url,headers=headers)
    if(r.status_code == 200) : 
        print(f'Statu code: {r.status_code}')
        return BS(r.content,'html.parser')
    else : 
        print("No connection")
        exit()
    
def get_marks(articles):
    marks = list()
    for article in articles:
        marks.append(article.find('div', class_='lenta-card').find('h3', class_='lenta-card__title').find('span', class_='lenta-card__mymark').text.strip())
    return marks

def get_names(articles):
    names = list()
    for article in articles:
        names.append(article.find('div', class_='lenta-card').find('div', class_='lenta-card-book__wrapper').find('a', class_='lenta-card__book-title').text.strip())
    return names
        
def get_comments_texts(articles):
    comments_texts = list()
    comments_urls = list()
    for article in articles:
        comments_urls.append(article.find('div', class_='review-card__footer footer-card').find('a', class_='footer-card__link').get('href'))
    for comment_url in comments_urls:
        comment_page_soup = get_page('https://www.livelib.ru' + comment_url)
        comments_texts.append(comment_page_soup.find('article', class_='review-card lenta__item').find('div', class_='lenta-card').find('div',class_='lenta-card__text without-readmore').text)
        
    return comments_texts
    
def save_comments(data, filename):
    for i in range(1,len(data)):
        file = open(filename+f'\\{i:04}'+'.txt', "w", encoding="utf-8")
        file.write(data[i].get_name())
        file.write('\n')
        file.write(data[i].get_comment())
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
        print(i)
        soup = get_page(url+'~'+str(i)+'#reviews')
        articles = soup.find('main', class_='main-body page-content').find('section', class_='lenta__content').findAll('article', class_='review-card lenta__item')
        
        #marks
        marks = get_marks(articles)
        
        #names
        names = get_names(articles)
        
        #texts
        comments_texts = get_comments_texts(articles)
        
        for j in range(len(marks)):
            condidate = Comment(names[j],comments_texts[j],float(marks[j]))
            
            if condidate.mark < 1: 
                zero+=1
            
            elif condidate.mark < 2.0 : 
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
                
        print(f'Zero = {zero} , One = {one}, Two = {two}, three = {three}, Four = {four}, Five = {five}')
        
        if zero>=least_num_of_marks and one>=least_num_of_marks and two>=least_num_of_marks and three>=least_num_of_marks and four>=least_num_of_marks and five>=least_num_of_marks:
            i=max_num_of_requests
            break
    
    return dataset
    
    
if __name__=="__main__":
    
    url = 'https://www.livelib.ru/reviews/'
    
    least_num_of_marks = 1000
    max_num_of_requests = 10000
            
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
    
    print("Работа окончена")
    
    
        
