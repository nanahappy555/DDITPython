import pymysql

class DaoStockOld:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='_stock_old', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selects(self,s_code):
        sql = f"""
            SELECT {s_code}
            FROM stock_sync_0121
        """
        # print("sql",sql)
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for i in rows:
            ret.append(i[s_code])
        return ret


    def selectAllNames(self):
        ret = []
        sql = """
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = '_stock_old'
            AND TABLE_NAME = 'stock_sync_0121'
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for r in rows:
            ret.append(r['COLUMN_NAME'])
        return ret
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    ret=[]
    dso = DaoStockOld()
    s_code = dso.selectAllNames()[0]
    print("s_code",s_code)
    list = dso.selects(s_code)
    print("list",list[0])
    
    
