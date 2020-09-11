import time
import requests
from bs4 import BeautifulSoup

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA"
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

#with open ("movie.html", "w") as f:
#    f.write(res.text)
#    f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)