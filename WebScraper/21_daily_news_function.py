import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def today_weather():
    url = "https://n.weather.naver.com/today"
    soup = create_soup(url)
    summary = soup.find("p", attrs={"class":"summary"}).get_text().strip()
    print(summary, "\n")


def today_headline():
    url = "https://news.naver.com/main/home.nhn"
    soup = create_soup(url)
    headlines = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)

    for idx, headline in enumerate(headlines):
        news = headline.find("div", attrs={"class":"hdline_article_tit"}).get_text()
        link = headline.a["href"] # == headline.find("a")["href"]
        print(f"{idx+1}. {news.strip()}")
        print(f"link : https://news.naver.com{link}", "\n")


def today_itnews():
    url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    itnews = soup.find("div", attrs={"class":"cluster_group _cluster_content"}).find_all("li")

    for idx in range(3):
        it = itnews[idx].find("div", attrs={"class":"cluster_text"}).find("a")
        link = it["href"]
        print(f"{idx+1}. {it.get_text().strip()}")
        print(f"link : {link}", "\n")


def today_english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print("=== English ===")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    
    print("\n", "=== Korean ===")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())


if __name__ == "__main__":
    print("[ Weather Summary ]")
    today_weather()
    print("\n")
    print("[ Headline News Top 3 ]")
    today_headline()
    print("\n")  
    print("[ IT News Top 3 ]")
    today_itnews()
    print("\n")  
    print("[ Today English ]")    
    today_english()


# Multi conditions
# dust = soup.find("dl", attrs={"class":"indicator", "id":"ust"}, text=["fine_dust", "ultra_fine_dust"])