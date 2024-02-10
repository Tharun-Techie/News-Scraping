import requests
from bs4 import BeautifulSoup as bs

# Requeest th fetch by link

url = 'https://www.dnaindia.com/business'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

responses = requests.get(url,headers=headers)

#parse the html doc

Soup = bs(responses.content,'html.parser')

# Extract the news headlines from news sites

headlines = Soup.find_all(class_='explainer-subtext')

with open('DnaIndia.txt','a') as f:
    for headline in headlines:
        f.write(headline.text + '\n')
