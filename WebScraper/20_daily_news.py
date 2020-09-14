import requests
from bs4 import BeautifulSoup

url1 = "https://n.weather.naver.com/today"
url2 = "https://news.naver.com/main/home.nhn"
url3 = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"

res1 = requests.get(url1)
res1.raise_for_status()

res2 = requests.get(url2)
res2.raise_for_status()

res3 = requests.get(url3)
res3.raise_for_status()

weather = BeautifulSoup(res1.text, "lxml")
headline = BeautifulSoup(res2.text, "lxml")
itnews = BeautifulSoup(res3.text, "lxml")


summary = weather.find("p", attrs={"class":"summary"}).get_text().strip()
print("========== Weather Summary ==========", "\n")
print(summary, "\n"*3)

news = headline.find("ul", attrs={"class":"hdline_article_list"}).find_all("li")
print("========== Headline News TOP 3 ==========", "\n")
for idx in range(3):
    hd = news[idx].find("div", attrs={"class":"hdline_article_tit"}).get_text()
    link = news[idx].find("a")["href"]
    print(f"{idx}. {hd.strip()}")
    print(f"link : https://news.naver.com{link}", "\n")


itnews = itnews.find("div", attrs={"class":"cluster_group _cluster_content"}).find_all("li")

print("\n"*2, "========== IT News TOP 3 ==========", "\n")
for idx in range(3):
    it = itnews[idx].find("div", attrs={"class":"cluster_text"}).find("a")
    link = it["href"]
    print(f"{idx}. {it.get_text().strip()}")
    print(f"link : {link}", "\n")
