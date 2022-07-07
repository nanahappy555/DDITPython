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
e_name = '5'
sex = '4'
addr = '4'

# f string은 python 3.5 이상부터 사용가능...
sql = f"""
    update emp
    set
        e_name = '{e_name}',
        sex = '{sex}',
        addr = '{addr}'
    where
        e_id = '{e_id}'
"""

cnt = cursor.execute(sql)
print(cnt)

conn.commit()
cursor.close()
conn.close()