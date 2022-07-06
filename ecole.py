# class ecole:
#
#     def __init__(self):
#         pass
import urllib3
from bs4 import BeautifulSoup
import requests

from urllib import request

url = "https://www.studapart.com/fr/logement-nos-ecoles-et-universites-partenaires?title=&page=%d"


def download(self, year):
    url = self.path + str(year) + self.filename
    r = requests.get(url)
    with open(self.BasePath + str(year) + ".csv.gz", "wb") as code:
        code.write(r.content)


if __name__ == '__main__':
    for i in range(0,23):
        # print(url % i)
        http = urllib3.PoolManager()

        resp = http.request('GET', url % i)
        html = resp.data.decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        # row = soup.find("div",{"class":"row"})
        articles = soup.find_all("article",{"class":"node"})
        print(len(articles))
        for article in articles:
            print(article["about"])
            # https: // www.studapart.com /
            src = article.find("img")["src"]

            print(src)
        break
