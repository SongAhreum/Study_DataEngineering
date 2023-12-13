import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url='https://www.google.com/search?q=%EC%86%A1%EC%A4%91%EA%B8%B0&tbm=isch&ved=2ahUKEwjPkOmFqvWCAxX_iFYBHQ2dAuAQ2-cCegQIABAA&oq=%EC%86%A1%EC%A4%91%EA%B8%B0&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABFAAWABgwwZoAHAAeACAAYgBiAGIAZIBAzAuMZgBAKoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=EYltZY_ECv-R2roPjbqKgA4&bih=743&biw=1763'

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})
print(len(images)) #header가 잘안들어가니까 안나오네 왜지?
for idx, image in enumerate(images):
    title=image.find('div', attrs={'class': 'zbRPDe M2qv4b P4HtKe'}).get_text()
    print(idx + 1, title)
    
    