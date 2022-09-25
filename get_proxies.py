import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

ua = UserAgent()

def proxy_request(url):
    counter = 0
    PROXY_CONDIDATES = get_free_proxies()
    while True:
        try:
            proxy = PROXY_CONDIDATES[counter]
            print(f'Try:{proxy}')
            proxies = {"http": proxy, "https": proxy}
            response = requests.get(url, proxies=proxies, timeout=10, headers={'User-Agent':ua.random})
            print(f"Proxy currently being used: {proxy['https']}")
            break
        except:
         print("Error, looking for another proxy")
        counter+=1
        print('\n')
    return response

def get_free_proxies():
    url = "https://hidemy.name/ru/proxy-list/"
    # получаем ответ HTTP и создаем объект soup
    soup = bs(requests.get(url).text, "html.parser")
    print(soup)
    proxies = list()
    rows = soup.find('div',class_='table_block').findAll("tr")[1:]
    for row in rows:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    print(proxies)
    return proxies

