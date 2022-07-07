import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       port=3305,
                       user='root',
                       password='python',
                       db='python',
                       charset='utf8'
                       )

cursor = conn.cursor()

e_id = '3'
sql= f"""
    delete from emp
    where e_id='{e_id}'
"""

cnt = cursor.execute(sql)

#확인용
print(cnt) # 여러행 확인 가능
# print(cursor.rowcount, "record inserted") # 1개 행만 확인됨 for문 돌려야할듯?

conn.commit()
cursor.close()
conn.close()