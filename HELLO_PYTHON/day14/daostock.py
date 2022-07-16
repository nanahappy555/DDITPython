import pymysql

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selects(self,s_name):
        ret = []
        sql = f"""
            select s_code,ymd,s_name,price from stock
            where
            s_name = '{s_name}'
        """
        # print("sql",sql)
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for r in rows:
            ret.append(r['price'])
        return ret

    def selectAllNames(self):
        ret = []
        sql = f"""
            select s_name from stock
            group by s_name
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for r in rows:
            ret.append(r['s_name'])
        return ret

    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoStock()
    list = de.selects('AJ네트웍스')
    list1 = de.selects('AJ네트웍스')[0]
    print("list",list)
    print("list1",list1)
    
    
    listname = de.selectAllNames()
    for idx,i in enumerate(listname):
        print(idx,i)
    
    
    
    
    