from turtle import title
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pandas as pd
from tqdm import tqdm


def scrapAll():
    page = 2
    scraptedData = []
    url_after = ['us-news','world','us/environment','football','us-news/us-politics','us/business','us/technology','science','sport/nfl','sport/tennis','books']
    for sub in url_after:

        page_url = f'https://www.theguardian.com/{sub}'
        html = requests.get(page_url).text
        soap = BeautifulSoup(html, 'lxml')
        links = soap.findAll("div", {"class": "fc-item__container"})
        # links = soap.find_all('h3')
        page += 1
        for link in tqdm(links):
            news_url = ''+link.a['href']
            try:
                article = Article(news_url)
                article.download()
                article.parse()
            except:
                print('fuck')
            scraptedData.append({
                'url': news_url,
                'text': article.text,
                'title': article.title
            })
        # if page == 150:
        #     break
        # print(links[2])

        # print(len(links))
    df = pd.DataFrame(scraptedData)
    df.to_csv(f'G2Page.csv')
    # print(scraptedData)


scrapAll()
