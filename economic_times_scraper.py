import requests
from bs4 import BeautifulSoup as bs

url = 'https://economictimes.indiatimes.com/markets/stocks/news'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

responses = requests.get(url,headers=headers)

#parse the html doc

soup = bs(responses.content,'html.parser')

#finding instances by div

stories = soup.find_all('div',class_='eachStory')

#Loop the to get each story

for story in stories:

    heading = story.find('h3').text.strip()

    paragraph = story.find('p').text.strip()

    print(f'Heading:{heading}')
    print(f'Story:{paragraph}')
    print()

    with open('op.txt','a',encoding='utf-8') as f:
        f.write(f'Heading:{heading} \n')
        f.write(f'Story:{paragraph} \n')
        f.write("  \n")
