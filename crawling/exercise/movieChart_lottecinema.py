

url ="https://www.lottecinema.co.kr/NLCHS/Movie/List?flag=1"


url = 'https://www.cgv.co.kr/'

# Session 생성
session = requests.Session()

# 요청 보내기
res = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)

# 오류 처리
try:
    res.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Oops, something went wrong:", err)

print(res.text)
soup = BeautifulSoup(res.text, "lxml")
title = soup.title.get_text()
print(title)