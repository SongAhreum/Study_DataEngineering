import requests
from bs4 import BeautifulSoup
import os
url="https://search.daum.net/search?w=tot&q=2022%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, "lxml")
image = soup.find_all('img',attrs={'class':'thumb_img'})

# movie 폴더가 없으면 생성
movie_folder = './lesson/data/movie_thumbnail'
if not os.path.exists(movie_folder):
    os.makedirs(movie_folder)


for index, image in enumerate(image):
  image_url = image['src']
  print(f'{index}:::{image_url}')
  
  image_res = requests.get(image_url)
  res.raise_for_status()
  with open('./lesson/data/movie_thumbnail/movie{}.jpg'.format(index),'wb') as f:
    f.write(image_res.content)