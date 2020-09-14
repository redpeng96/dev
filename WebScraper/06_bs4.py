import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#print(soup.title.get_text())
#print(soup.a.attrs)

#print(soup.find("a", attrs={"class":"Nbtn_upload"}).get_text())
#print(soup.find(attrs={"class":"Nbtn_upload"}))

rank1 = soup.find("li", attrs={"class":"rank01"})

# Multi conditions
# dust = soup.find("dl", attrs={"class":"indicator", "id":"ust"}, text=["fine_dust", "ultra_fine_dust"])

#print(rank1.parent.get_text())\

#print(rank1.find_next_sibling("li").a.get_text())

#rank2 = rank1.find_next_sibling("li")
#print(rank2.a.get_text())
ranks = rank1.find_next_siblings("li")
print(ranks)