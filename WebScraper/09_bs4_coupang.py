import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    if item.find("span", attrs={"class":"ad-badge-text"}):
        #print("< AD PRODUCTS >")
        continue
    name = item.find("div", attrs={"class":"name"}).get_text()
    if "Apple" in name:
        print("NO APPLE")
        continue 
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        #print("No Rate")
        continue

    reviews = item.find("span", attrs={"class":"rating-total-count"})    
    if reviews:
        reviews = reviews.get_text()
    else:
        #print("(No Reviews)")
        continue
    if float(rate) > 4.5 and int(reviews[1:-1]) >= 100:
        print(name, "/ $" + price, "/ " + rate, reviews)
    else:
        continue