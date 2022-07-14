import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5000/'

html = requests.get(url)

print(html) # <Response [200]>
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
trs = soup.select("tr")

for idx,tr in enumerate(trs): # 배열 foreach
    if idx > 0: # 헤더(사원,이름,성별,주소) 제외
        tds = tr.select("td")
        print(idx,tds[1].text,tds[3].text,"----------------------")
        
"""
<tr>
        <td><a href="emp_detail?e_id=2">2</a></td> tds[0]
        <td>시진핑</td>                              tds[1]
        <td>2</td>                                 tds[2]
        <td>중국 베이징시 자금성 101호</td>              tds[2]
    </tr>
"""