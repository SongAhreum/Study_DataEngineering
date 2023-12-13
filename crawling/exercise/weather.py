import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

url = 'https://weather.naver.com/today/02171581?cpName=KMA'

def fn_soup(url):
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text,'lxml')
  return soup

def scrap_wheather():
  soup = fn_soup(url);
  #현재온도
  current_temper = soup.find('strong',attrs={'class':'current' })
  current_temper = current_temper.text.strip()
  current_temper = re.search(r'([\d.]+)°', current_temper).group(1)#숫자만
  #체감 온도
  
  #현재 습도
  
  #현재 풍속
  
  #현재 미세먼지
  
  #현재 초미세먼지
  
  #일출시각
  
def makeOptions():
  options = webdriver.ChromeOptions();
  options.headless = True
  options.add_argument('headless')
  return options  
def tommorow_summary():
  browser = webdriver.Chrome(options=makeOptions())
  browser.maximize_window()
  browser.get(url)
  
  btn_tommorow_summary = browser.find_element(By.CLASS_NAME,'btn_next')
  btn_tommorow_summary.click()
  
  
  
if __name__ == "__main__":
  scrap_wheather() 
  