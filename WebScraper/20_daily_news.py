import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#with open("daum.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify)

items = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for idx, item in enumerate(items):
    column = item.find_all("td")
    print("========== 매물 {} ==========".format(idx+1))
    print(f"거래 : {column[0].get_text().strip()}")
    print(f"면적: {column[1].get_text().strip()} (공급/전용)")
    print(f"가격 : {column[2].get_text().strip()} (만원)")
    print(f"동 : {column[3].get_text().strip()}동")
    print(f"층: {column[4].get_text().strip()}", "\n")
    
