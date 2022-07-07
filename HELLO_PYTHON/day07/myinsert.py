import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       port=3305,
                       user='root',
                       password='python',
                       db='python',
                       charset='utf8'
                       )

cursor = conn.cursor()

data = [3,'3','3','3']
sql_insert = """insert into emp(e_id, e_name, sex, addr) 
                values (%s, %s, %s, %s)"""

cnt = cursor.execute(sql_insert, data)
# cnt += cursor.execute(sql_insert, (4,'4','4','4')) #매개변수로
# cnt += cursor.execute(sql_insert, (5,'4','4','4')) #매개변수로

#확인용
print(cnt) # 여러행 확인 가능
# print(cursor.rowcount, "record inserted") # 1개 행만 확인됨 for문 돌려야할듯?

conn.commit()
cursor.close()
conn.close()