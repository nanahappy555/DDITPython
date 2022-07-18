import requests
from bs4 import BeautifulSoup
from _datetime import datetime
from daostock import DaoStock

ds = DaoStock()

now = datetime.now()
ymd = now.strftime("%Y%m%d.%H%M")

url = 'https://vip.mk.co.kr/newSt/rate/item_all.php'

html = requests.get(url)
html.encoding='EUC-KR'


soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td","st2")

for idx,td in enumerate(tds):
    s_name = td.text
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text.replace(',',"") # td의 부모(tr)의 하위태그 td중 1번째idx의 text
    cnt = ds.insert(s_code, ymd, s_name, price)
    print(idx,"cnt",cnt)

