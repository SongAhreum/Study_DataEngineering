import requests
from bs4 import BeautifulSoup

url = "https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=41&p=1"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
items =  soup.find_all('div',attrs={'class':'box__item-container'})
#print(len(items))
for i,item in enumerate(items):
  #------------------------상품명
  name = item.find('span',attrs={'class':'text__item'})['title']
  #------------------------가격
  price = item.find('strong',attrs={'class':'text text__value'}).get_text()
  # print(str(i)+"번째=============="+price)
  #print(f'{i}:{price}')
  #------------------------평점
  rate = item.find('span',attrs={'class':'image__awards-points'})
  if rate:
    rate = rate['style']
    index = rate.find(':')+1
    rate = rate[index:]
  else :
    rate='평점없음'  
  #------------------------리뷰수
  count = item.find('li',attrs={'class':'list-item list-item__feedback-count'})
  if count:
    count = count.find('span',attrs={'class':'text'}).get_text()
    count = count.replace('(',"").replace(')',"").replace(',','')
  else:
    count = '리뷰없음'
  
  image_tag = item.find('img')
  
  # if image_tag and 'srcset' in image_tag.attrs:
  print(image_tag)
  #   srcset = image_tag['srcset']
  #   # srcset을 콤마(,)로 분리하고 첫 번째 이미지 주소만 선택
  #   image_url = srcset.split(',')[0].strip().split(' ')[0]
  #   print(image_url)
  #   image = 'http:'+image_url
  # else:
  #   print('이미지가 없습니다.')
  
  
      
  #print(f'{i}:name:{name}//////price:{price}//////rate:{rate}//////count:{count}//////\n{image}')  
    