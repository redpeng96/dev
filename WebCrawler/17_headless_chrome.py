import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# Headless Chrome settings
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")
browser = webdriver.Chrome("./chromedriver", options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA"

browser.get(url)

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("Scroll Finished!!!")


# Create screenshot
browser.get_screenshot_as_file("gmovie.png")


soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    org_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if org_price:
        org_price = org_price.get_text()
    else:
        continue

    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    
    print("TITLE: " + title)
    print("Org Price: "+ org_price, "/", "Price: " + price)
    print("https://play.google.com" + link)
    print("-" * 100, "\n")

time.sleep(2)
browser.quit()