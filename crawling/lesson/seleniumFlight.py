from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url ="https://flight.naver.com/"
browser = webdriver.Chrome()
browser.get(url)

#도착지선택
local = browser.find_element(By.XPATH,'//b[text()="도착"]')
local.click()
time.sleep(3)
domestic = browser.find_element(By.XPATH,'//button[text()="국내"]')
domestic.click()
time.sleep(3)

jeju = browser.find_element(By.XPATH,'//i[text()="제주국제공항"]')
jeju.click()
time.sleep(3)


#여행일자선택
depart=browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[4]/div/div/div[2]/div[2]/button[1]')
depart.click()
time.sleep(2)
#가는날 선택
# day25 = browser.find_elements(By.XPATH,'//b[text()=="25"][0]')
day25 = browser.find_elements(By.XPATH,'//b[text()="25"]')
day25[0].click()
time.sleep(2)
#돌아오는날선택
day28 = browser.find_elements(By.XPATH,'//b[text()="28"]')
day28[0].click()
time.sleep(1)

# ##이렇게도됨
# local = browser.find_element(By.CLASS_NAME,'select_name__1L61v')
# local.click()
# time.sleep(3)



#항공권검색
search = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
search.click()
time.sleep(3)

#안되는코드임
# first = '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div/button'
# elem = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,first)))
# #presence_of_element_located는 튜플형태로 사용해야한다
# time.sleep(3)
# print(elem.text)

first = '//div[@class="domestic_Flight__sK0eA result"]'
elem=WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, first)))
print(elem.text)
