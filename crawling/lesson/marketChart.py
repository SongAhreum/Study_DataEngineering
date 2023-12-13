import requests
from bs4 import BeautifulSoup

def fn_soup(text): 
  soup = BeautifulSoup(text, "lxml")

  items = soup.find_all('div', attrs={'class' : 'box__item-container'})
  print((len(items)))

  #print("-"*50)
  seq = 0
  for i, item in enumerate(items):
      # 각 상품의 이름
      name = item.find('span', attrs = {'class':'text__item'})['title']
      
      # 각 상품의 가격
      price = item.find('strong', attrs = {'class':'text text__value'}).get_text()
      
      # 각 상품의 평점 (style 속성에서 추출)
      rate = item.find('span', attrs = {'class':'image__awards-points'})
      if rate:
          rate = rate['style']
          index = rate.find(':') + 1   # ":" 다음의 문자부터가 실제 평점 정보이므로 해당 인덱스를 찾음
          rate = rate[index:]   # 찾은 인덱스부터 끝까지를 평점으로 설정
          rate = rate[:-1]   # 맨 끝의 '%' 기호를 제거
      else:
          #rate = "평점없음"
          continue

      # 각 상품의 피드백 수
      count = item.find('li', attrs = {'class' : 'list-item list-item__feedback-count'})
      if count:
          count = count.find('span', attrs = {'class' : 'text'}).get_text()
          count = count.replace('(','').replace(')','').replace(',', '')
      else:
          #count = '피드백수 없음'
          continue
      
      #https://gdimg.gmarket.co.kr/2896243670/still/280?ver=1698717144  
      #image = 'https:' + item.find('img')['src']
      
      # 평점 90점 이상 300보다
      if int(rate) >= 90 and int(count) >= 300:
          seq = seq + 1
          print(f'{seq}. [{name}] : {price}원 , 평점:{rate} , 피드백수:{count}\n')
  
for i in range(1, 6):
  print(i, '-' * 100)
  url = "https://browse.gmarket.co.kr/search?keyword=모니터&k=41&p={}".format(i)
  res = requests.get(url) 
  res.raise_for_status() 
  fn_soup(res.text)      