import requests
import bs4
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')


for article in articles:
    article_preview = article.find(class_ = 'tm-article-snippet').text
    article_preview_text = re.sub(r'[,.!?@$%^&*()"<>«»\[\]]', '', article_preview)
    if set(word.lower() for word in KEYWORDS) & set(article_preview_text.lower().split()):
        href = article.find(class_ = 'tm-article-snippet__title-link').attrs['href']
        link = 'https://habr.com/' + href
        print(f"{article.find(class_ = 'tm-article-snippet__datetime-published').find('time')['title']} - {article.find('h2').text} - {link}")