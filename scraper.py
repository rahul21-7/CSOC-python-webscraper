import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://github.com/trending"
html = requests.get(URL)
soup = BeautifulSoup(html.content, 'html.parser')

page_title = soup.title.text
print(page_title,"\n")

articles = soup.find_all('article')

df = pd.DataFrame(columns=['Owner', 'Item'])

for article in articles[:5]:
    anchor = article.select('a')
    item = anchor[1].text.strip()
    owner = ""
    i = 0
    while item[i] != '/':
        owner += item[i]
        item = item[1:]
    
    while item[0] == ' ' or item[0] == '\n' or item[0] == '/':
        item = item[1:]
    # print(f"Owner: {owner}")
    # print(f"Item: {item.strip()}")

    df = df._append({'Owner':owner,'Item':item}, ignore_index=True)


print(df)
# Save the DataFrame to a CSV file
df.to_csv('trending_repositories.csv', index=True)
