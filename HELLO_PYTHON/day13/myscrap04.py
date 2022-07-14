import requests
from bs4 import BeautifulSoup
from _datetime import datetime
from day13.daostock import DaoStock

ds = DaoStock()

now = datetime.now()
ymd = now.strftime("%Y%m%d.%H%M")

url = 'https://vip.mk.co.kr/newSt/rate/item_all.php'

html = requests.get(url)
html.encoding='EUC-KR'

# print(html) # <Response [200]>
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td","st2")
# print(ymd)

# for td in tds:
# enumerate로 돌리면 idx를 추가할 수 있고 idx로 어느 행에서 에러가 나는지 확인 가능함
for idx,td in enumerate(tds):
    s_name = td.text
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text.replace(',',"") # td의 부모(tr)의 하위태그 td중 1번째idx의 text
    cnt = ds.insert(s_code, ymd, s_name, price)
    print(idx,"cnt",cnt)

