import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()
browser.get("https://flight.naver.com/flights/")

browser.find_element_by_link_text('도착').click()
browser.find_element_by_link_text('제주').click()

browser.find_element_by_link_text('가는날 선택').click()
browser.find_element_by_link_text('다음달').click()

browser.find_elements_by_link_text('27')[0].click()
browser.find_elements_by_link_text('29')[0].click()

browser.find_element_by_link_text('항공권 검색').click()

# wait until the element is appeared, and then run the next line and move to "finally:".
# If fail to find the element within 10sec, it will move to "finally:".
try:
    elem = WDWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
    time.sleep(3)
finally:
    browser.quit()

