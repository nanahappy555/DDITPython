import requests
from bs4 import BeautifulSoup

url = 'https://vip.mk.co.kr/newSt/rate/item_all.php'

html = requests.get(url)
html.encoding='EUC-KR'

# print(html) # <Response [200]>
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td","st2")

for td in tds:
    s_name = td.text
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text # td의 부모(tr)의 하위태그 td중 1번째idx의 text
    print(s_name,s_code,price)

# print(td)