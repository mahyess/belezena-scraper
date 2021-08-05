from bs4 import BeautifulSoup
import requests
import csv


class Scraper:
    def __init__(self, get_count):
        self.count = get_count
        pass

    def fetch(self, url, data=None):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US;en;q=0.5",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "www.belezanaweb.com.br",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-GPC": "1",
            "TE": "trailers",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36",
        }
        with requests.Session() as s:
            if data is None:
                return s.get(url, headers=headers).content
            else:
                return s.post(url, data=data).content

    def get_categories(self):
        url = "https://belezanaweb.com.br/institucional/marcas/"

        content = self.fetch(url)
        soup = BeautifulSoup(content, "lxml")

        categories = soup.find_all("li", {"class": "sub-menu-item"})

        for i, category in enumerate(categories):
            if category.parent.get("class", None):
                # this just starting characters, can be ignored.
                del categories[i]

        return [
            {
                "title": category.find("a").text.strip(),
                "url": f"https://belezanaweb.com.br/api/htmls/showcase?uri={category.find('a')['href']}&tab=produtos&size=36",
            }
            for category in categories
        ]

    def get_items(self, category):
        with open(f'results/{category["title"]}.csv', mode="w") as csv_file:
            fieldnames = ["link", "title", "photo", "brand", "price"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            i = 0

            page = 1

            while page:
                url = f"{category['url']}&pagina={page}"
                soup = BeautifulSoup(self.fetch(url), "lxml")

                items = soup.find_all("div", {"class": "showcase-item"})

                for item in items:
                    self.count(i)
                    i += 1
                    details = {
                        "link": "",
                        "title": "",
                        "photo": "",
                        "brand": "",
                        "price": "",
                    }

                    details["link"] = item.find("a", {"class": "showcase-item-title"})[
                        "href"
                    ]
                    details["title"] = item.find(
                        "a", {"class": "showcase-item-title"}
                    ).text.strip()
                    details["photo"] = item.find("img")["data-src"]
                    details["brand"] = item.find(
                        "span", {"class": "showcase-item-brand"}
                    ).text.strip()
                    details["price"] = item.find(
                        "span", {"class": "price-value"}
                    ).text.strip()

                    print(details["title"])

                    details["title"] = details["title"].encode("utf-8")
                    details["photo"] = (
                        details["photo"]
                        .replace("w_210", "w_800")
                        .replace("h_210", "h_800")
                    )

                    writer.writerow(details)

                if len(items):
                    page += 1
                    # i += len(items)
                else:
                    page = 0
