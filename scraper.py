import requests
from bs4 import BeautifulSoup

URL = "https://github.com/trending"
html = requests.get(URL)
soup = BeautifulSoup(html.content, 'html.parser')

page_title = soup.title.text
print(page_title,"\n")

articles = soup.find_all('article')
for article in articles[:5]:
    anchor = article.select('a')
    print(anchor[1].text.strip(),"\n")
    print("--------------------------------------------------------\n")