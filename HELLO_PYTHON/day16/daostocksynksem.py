import numpy as np
import pymysql

class DaoStockSink:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='_stock_old', charset='utf8')
 
        self.curs = self.conn.cursor()

    def selects(self):
        sql = f"""
            select * from stock_sync_0121
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        
        row_c = []
        for r in rows:
            len_r = len(r)
            row_c.append(r[:len_r-1]) # time 컬럼을 잘라냈음
        
        rows_n = np.array(row_c) # 1 2
        rows_t = np.transpose(rows_n) # 1111 2222
        return rows_t


    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    dss = DaoStockSink()
    list = dss.selects()
    print("len",len(list))
    for idx,tu in enumerate(list):
        print(idx,tu)
    
    
    
    
    