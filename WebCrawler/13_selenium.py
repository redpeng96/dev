import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver")

# move to NAVER
browser.get("http://www.naver.com")

# Click login button
elem = browser.find_element_by_class_name("link_login")
elem.click()

# Input ID/Pass and click ENTER
browser.find_element_by_id("id").send_keys("test")
browser.find_element_by_id("pw").send_keys("test")

browser.find_element_by_id("log.login").click()

time.sleep(3)

# Re-input ID
browser.find_element_by_id("id").clear
browser.find_element_by_id("id").send_keys("test222")


print(browser.page_source)

time.sleep(5)

browser.quit()

