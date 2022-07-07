import pymysql
class DaoEmp:
    
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3305,
            user='root',
            password='python',
            db='python',
            charset='utf8'
            )
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selects(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
    
    def select(self,e_id):
        sql = f"""
            select e_id, e_name, sex, addr
            from emp 
            where e_id='{e_id}'
            """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows[0] # []가 나오지않음
    
    def insert(self,e_name,sex,addr):
        sql = f"""
            insert into emp(e_name,sex,addr)
            values ('{e_name}','{sex}','{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,e_id,e_name,sex,addr):
        sql = f"""
            update emp
            set
                e_name = '{e_name}',
                sex = '{sex}',
                addr = '{addr}'
            where
                e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
        delete from emp
        where e_id = '{e_id}' 
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    # rows = de.selects()
    # emp = de.select(1)
    # cnt = de.insert('13','1','1')
    # cnt2 = de.update(6,'수정','6','6')
    cnt3 = de.delete(5)
    print("성공한 행 개수 : ",cnt3)