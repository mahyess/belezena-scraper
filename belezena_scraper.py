from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.belezanaweb.com.br/institucional/marcas/'

s = requests.Session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4491.0 Safari/537.36'
}

def fetch(url, data=None):
    if data is None:
        return s.get(url, headers=headers).content
    else:
        return s.post(url, data=data).content

content = fetch(url)
soup = BeautifulSoup(content, 'lxml')

categories = soup.find_all("li", {"class": "sub-menu-item"})

with open('result.csv', mode='w') as csv_file:
    fieldnames = ['link', 'title', 'photo', 'brand', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for category in categories:
        if category.parent.get('class', None):
            # this just starting characters, can be ignored.
            pass
        page = 1

        while page:
            url = f"https://www.belezanaweb.com.br/api/htmls/showcase?uri={category.find('a')['href']}&tab=produtos&size=36&pagina={page}"
            category_soup = BeautifulSoup(fetch(url), 'lxml')

            items = category_soup.find_all("div", {"class": "showcase-item"})

            for item in items:
                details = {
                    "link": "",
                    "title": "",
                    "photo": "",
                    "brand": "",
                    "price": ""
                }

                details["link"] = item.find("a", {"class": "showcase-item-title"})["href"]
                details["title"] = item.find("a", {"class": "showcase-item-title"}).text.strip()
                details["photo"] = item.find("img")["data-src"]
                details["brand"] = item.find("span", {"class": "showcase-item-brand"}).text.strip()
                details["price"] = item.find("span", {"class": "price-value"}).text.strip()

                print(details["title"])

                writer.writerow(details)
            
            if len(items):
                page += 1
            else:
                page = 0
