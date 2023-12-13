import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def makeOptions():
  options = webdriver.ChromeOptions();
  options.headless = True
  options.add_argument('headless')
  return options

def fn_soup(res):
  # soup = BeautifulSoup(res.text, "lxml")
  soup = BeautifulSoup(res, "lxml")
  images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})
  print(len(images)) #header가 잘안들어가니까 안나오네 왜지?
  for idx, image in enumerate(images):
      title=image.find('div', attrs={'class': 'zbRPDe M2qv4b P4HtKe'}).get_text()
      print(idx + 1, title)


###################

browser = webdriver.Chrome(options=makeOptions())
browser.maximize_window()

url='https://www.google.com/search?q=%EC%86%A1%EC%A4%91%EA%B8%B0&tbm=isch&ved=2ahUKEwjPkOmFqvWCAxX_iFYBHQ2dAuAQ2-cCegQIABAA&oq=%EC%86%A1%EC%A4%91%EA%B8%B0&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABFAAWABgwwZoAHAAeACAAYgBiAGIAZIBAzAuMZgBAKoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=EYltZY_ECv-R2roPjbqKgA4&bih=743&biw=1763'
browser.get(url)

#이전 스크롤 높이
prev_height = browser.execute_script('return document.body.scrollHeight')
print('이전높이',prev_height)

while True:
  browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  time.sleep(2)
  curr_height = browser.execute_script('return document.body.scrollHeight');
  if prev_height == curr_height:
    break
  else:
    prev_height = curr_height

res = browser.page_source
time.sleep(1)
fn_soup(res)
time.sleep(2)


