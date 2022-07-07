# mysql라이브러리를 가져와서 emp테이블의 데이터 출력하기 (1111,2222)
# 검색 키워드는 mysql로 한다. mysql과 mariaDB는 거의 비슷하다.

import pymysql

# db연결하기
conn = pymysql.connect(
    host='127.0.0.1',
    port=3305,
    user='root',
    password='python',
    db='python',
    charset='utf8'
)

# 커서 설정
cursor = conn.cursor()

# sql문을 cursor.execute(쿼리문)로 실행
sql = "select * from emp"
cursor.execute(sql)
result = cursor.fetchall() 
"""
fetchall() 모든 데이터를 한 번에 가져올 때
fetchone() 한번 호출에 하나의 행만 가져올 때
fetchmany(n) n개만큼의 데이터를 가져올 때
"""

# 출력
print(result)

#자원반납
cursor.close() #cursor 닫아줌
conn.close() # with를 쓰면 close할 필요가 없다

