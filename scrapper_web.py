import requests
from bs4 import BeautifulSoup

#BeautifulSoup documentation
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/


UK_news_url = 'https://www.theguardian.com/uk'
# Baixando os links dos diferentes temas
html_data = requests.get(UK_news_url).text
soup = BeautifulSoup(html_data, 'html.parser')
url_topics = [el.find('a')['href'] for el in soup.find_all(class_='subnav__item')[1:9]]
topics = [el.text.strip('\n').replace(' ', '_') for el in soup.find_all(class_='subnav-link')[1:9]]
for i in range(len(topics)):
    print('Topic {}: {} ({})'.format(i + 1, topics[i], url_topics[i]))


# Obtendo a segunda noticia do primeiro tema [1]
html_data = requests.get(url_topics[0]).text
soup = BeautifulSoup(html_data, 'html.parser')
article_title = soup.find_all(class_='fc-item')[1].find('a').text
article_url = soup.find_all(class_='fc-item')[1].find('a')['href']
print(article_title)
print(article_url)

# Obtendo o conteudo da noticia escolhida
html_data = requests.get(article_url).text
soup = BeautifulSoup(html_data, 'html.parser')
article_full_title = soup.find('h1').text
article_text = soup.find('article').text
article_image = soup.find_all('figure')[0].find('img')['src']
print(article_full_title)
print(article_image)
print(article_text)