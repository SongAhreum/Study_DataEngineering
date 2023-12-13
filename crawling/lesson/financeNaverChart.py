import requests
from bs4 import BeautifulSoup
import csv
import os

# movie 폴더가 없으면 생성
movie_folder = './lesson/data/finance'
if not os.path.exists(movie_folder):
    os.makedirs(movie_folder)
file = open('./lesson/data/finance/시가총액1-200.csv','w',encoding='utf-8' ,newline='')
writer = csv.writer(file)
title ='#No	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
writer.writerow(title)

def fn_data(soup):
  data = soup.find('table',attrs={'class':'type_2'}).find('tbody')
  data_rows = data.find_all('tr')

  for row in data_rows:
    columns = row.find_all('td')
    if(len(columns)) <=1:
      continue
    data = [col.get_text().strip() for col in columns]
    print(data)
    writer.writerow(data)


for page in range(1,5):
  url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'lxml')
  fn_data(soup)


    