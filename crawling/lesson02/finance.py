import requests
from bs4 import BeautifulSoup
import csv
import os

URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"
FILE_PATH = './lesson02/data'
FILE_NAME = '시가총액.csv'
TITLE = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')

def fn_soup(url):
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text,'lxml')
  tbody = soup.find('table',attrs={'class':'type_2'}).find('tbody')
  rows = tbody.find_all('tr') 
  print(len(rows))

  for row in rows:
    cols= row.find_all('td')
    if len(cols) <= 1:
      continue
    data = [col.get_text().strip() for col in cols]  
    # [print(t) for t in data]
  return data

def mkdir(path):
  if not os.path.exists(path):
    os.makedirs(path)

def file_write(data,file_path,file_name,title):
  pullpath = file_path+'/'+file_name
  file = open(pullpath,'w',encoding='utf-8',newline="")
  writer = csv.writer(file)
  writer.writerow(title)
  writer.writerow(data)
  
def run():
  data = fn_soup(URL)  
  mkdir(FILE_PATH)
  file_write(data,FILE_PATH,FILE_NAME,TITLE)
if __name__ == "__main__":
  run()     