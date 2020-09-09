import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
#cartoons = soup.find_all("td", attrs={"class":"title"})

#for cartoon in cartoons:
#    title = cartoon.a.get_text()
#   link = cartoon.a["href"]
#    print(title, "https://comic.naver.com" + link)


total = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.strong.get_text()
    total += float(rate)
total_rate = total / len(cartoons)
print("%0.2f" % total_rate )