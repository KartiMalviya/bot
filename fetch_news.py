import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = "https://slrtce.in/"  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_list = []
    for article in soup.find_all('div', class_='news-item'):
        title = article.find('h2').text
        link = article.find('a')['href']
        date = article.find('span', class_='date').text
        news_list.append({'title': title, 'link': link, 'date': date})

    return news_list
