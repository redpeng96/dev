import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()



#from selenium import webdriver
#from selenium.webdriver.common.keys import keys
#browser = webdriver.Chrome("./chromedriver")
#browser.get("http://naver.com")
#elem = browser.find_element_by_class_name("link_login")
#elem.click()
#browser.back()
#browser.forward()
#browser.refresh()

#elem2 = browser.find_element_by_id("query")
#elem2.send_keys("google")
#elem2.send_keys(Keys.ENTER)

#elems = browser.find_elements_by_tag_name("a")
#for e in elems:
#    e.get_attribute("href")

#elem3 = browser.find_element_by_xpath("//*[@id='search_btn']/span[2]")
#elem3.click()