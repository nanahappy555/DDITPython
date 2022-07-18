import pymysql
class DaoStock:
    
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3305,
            user='root',
            password='python',
            db='python',
            charset='utf8'
            )
        self.curs = self.conn.cursor(pymysql.cursors.SSDictCursor)
        
    
    def insert(self,s_code,ymd,s_name,price):
        sql = f"""
            insert into stock
                (s_code,ymd,s_name,price)
            values
                ('{s_code}','{ymd}','{s_name}','{price}')
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()