import requests
import re
from bs4 import BeautifulSoup

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})
names = soup.find_all("div", attrs={"class":"info_tit"})

for idx, image in enumerate(images):
    name = names[idx].get_text()
    img_url = image["src"]
    if img_url.startswith("//"):
        img_url = "https:" + img_url
        print(img_url)
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open("2019_movie_images0{}_{}.jpg".format(idx+1, name), "wb") as f:
            f.write(img_res.content)
        if idx >= 4:
            break
    else:
        continue
