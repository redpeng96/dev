import requests
import re
from bs4 import BeautifulSoup

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
#for i in range(9, 4, -1):
for i in range(9, 4, -1):
    url = "https://search.daum.net/search?w=tot&q=201{}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(i)
    #print(url)

    res = requests.get(url, headers=header)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class":"thumb_img"})
    name = soup.find("a", attrs={"class":"tit_main"}).get_text()

    for idx, image in enumerate(images):
        img_url = image["src"]
        if img_url.startswith("//"):
            img_url = "https:" + img_url
            print(img_url)
            img_res = requests.get(img_url)
            img_res.raise_for_status()

            with open("201{}_movie_images0{}_{}.jpg".format(i, idx+1, name), "wb") as f:
                f.write(img_res.content)
            if idx >= 4:
                break
        else:
            continue
